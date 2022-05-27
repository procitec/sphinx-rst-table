from docutils.parsers.rst import Directive, directives, nodes
from sphinx import addnodes
from sphinx.directives import ObjectDescription
from sphinx.errors import ExtensionError
from sphinx.util import logging

logger = logging.getLogger(__name__)

import sys
import re

_module = sys.modules[__name__]
_module.tables = {}
_module.rows = {}
_module.table_id = 0
_module.row_id = 0


class TableDirective(ObjectDescription):
    """A custom directive that describes a table in the tbl domain.

    Builds a need based on a given layout for a given need-node.

    The created table must have the following docutils structure::

        - table
        -- tgroup
        --- colspec (partial used)
        --- thead (not used)
        --- tbody
        ---- row
        ----- entry
        ------ custom layout nodes
    """

    has_content = True
    required_arguments = 1
    option_spec = {
        "headers": directives.unchanged,
        "widths": directives.unchanged,
        "title": directives.unchanged,
        "columns": directives.unchanged,
        "class": directives.unchanged,
    }

    def run(self):
        env = self.env
        classes = ["tbl"]

        if "class" in self.options:
            classes.append(self.options["classes"])

        headers = []
        widths = []
        columns = None
        table_id = None
        caption = self.arguments[0]

        logger.debug(f"got caption {caption}")
        ids = [f"table-{caption}"]

        if "id" in self.options:
            table_id = self.options["id"]
            ids.append(f"table-{table_id}")

        node_table = nodes.table(classes=classes, ids=ids)

        if "title" in self.options:
            node_caption = nodes.title(text=caption)
            node_table += node_caption

        if "headers" in self.options and 0 < len(self.options["headers"]):
            headers = re.split(",\s{0,1}", self.options["headers"] )
            logger.debug(f"found {len(headers)} entries in header")
            columns = len(headers)
        if "widths" in self.options and 0 < len(self.options["widths"]):
            widths = re.split(",\s{0,1}", self.options["widths"] )
            logger.debug(f"found {len(widths)} entries in widths")
            columns = len(widths)
        if "columns" in self.options:
            columns = int(self.options["columns"])
            if env.config.rst_table_autonumber:
                columns += 1
        elif "headers" not in self.options and "widths" not in self.options:
            raise ExtensionError(
                "could not determine number of columns from header or widths options. 'columns' options must be given"
            )

        logger.debug(f"create table with {columns} columns")

        if env.config.rst_table_autonumber_reset_on_table:
            _module.table_id = 0

        _module.row_id = 0
        _module.table_id += 1

        node_tgroup = nodes.tgroup(cols=columns)
        node_table += node_tgroup

        # todo match headers and widths length to match together
        if 0 < len(widths):
            for width in widths:
                logger.debug(f"create colspec with {int(width)} column")
                node_colspec = nodes.colspec(colwidth=int(width))
                node_tgroup += node_colspec
        else:
            for i in range(0, columns):
                logger.debug(f"create colspec with {int(100/columns)} column")
                node_colspec = nodes.colspec(colwidth=int(100 / columns))
                node_tgroup += node_colspec

        if 0 < len(headers):
            header_row = nodes.row()
            for header in headers:
                header_row += nodes.entry("", nodes.paragraph(text=header))

            node_thead = nodes.thead("", header_row)

        node_tbody = nodes.tbody()
        self.state.nested_parse(self.content, self.content_offset, node_tbody)
        node_tgroup += node_tbody

        if 0 < len(headers):
            node_tgroup += node_thead

        if caption is not None or table_id is not None:
            tbl = self.env.get_domain("tbl")
            tbl.add_table(caption, table_id)
        return [node_table]


class RowDirective(ObjectDescription):
    """A custom directive that describes a row in a table in the tbl domain.

    Builds a need based on a given layout for a given need-node.

    The created table must have the following docutils structure::

        - table
        -- tgroup
        --- colspec (partial used)
        --- thead (not used)
        --- tbody
        ---- row
        ----- entry
        ------ custom layout nodes
    """

    has_content = True
    required_arguments = 0
    option_spec = {
        "id": directives.unchanged,
        "class": directives.unchanged,
    }

    def run(self):
        env = self.env
        classes = ["tbl-row"]
        ids=[]

        # todo add odd/even to clases
        if "class" in self.options:
            classes.append(self.options["classes"])

        _module.row_anchor = None
        
        if "id" in self.options:
            _module.row_anchor = f"row-{self.options['id']}"
            logger.debug(f"storing row anchor row-{_module.row_anchor}")

        content_row = nodes.row(classes=classes)
        _module.row_id += 1

        if env.config.rst_table_autonumber:
            if _module.row_anchor is not None:
                ids.append(_module.row_anchor)
                _module.row_anchor = None
            node = nodes.entry(classes=classes, ids=ids)
            node_id = nodes.Text(f"{_module.table_id}.{_module.row_id}")
            node += node_id
            if "id" in self.options:
                logger.debug(f"adding row with id {self.options['id']} to domain")
                tbl = self.env.get_domain("tbl")
                tbl.add_row(self.options["id"])

            content_row += node

        self.state.nested_parse(self.content, self.content_offset, content_row)

        return [content_row]


class ColumnDirective(ObjectDescription):
    """A custom directive that describes a column in a table in the tbl domain."""

    has_content = True
    required_arguments = 0
    option_spec = {
        "class": directives.unchanged,
    }

    def run(self):
        classes = ["tbl-col"]
        # todo add odd/even to clases
        if "class" in self.options:
            classes.append(self.options["classes"])

        logger.debug(f"adding column with content {self.content}")
        self.assert_has_content()
        ids = []
        
        if _module.row_anchor is not None:
            ids.append(_module.row_anchor)
            _module.row_anchor = []
        
        node = nodes.entry(classes=classes, ids=ids)
        self.state.nested_parse(self.content, self.content_offset, node)
        return [node]
