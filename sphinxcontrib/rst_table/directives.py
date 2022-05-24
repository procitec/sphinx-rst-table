from docutils.parsers.rst import directives
from docutils.parsers.rst import nodes

from sphinx import addnodes
from sphinx.directives import ObjectDescription
from docutils.parsers.rst import Directive

from sphinx.util import logging
logger = logging.getLogger(__name__)

import sys

_module = sys.modules[__name__]
_module.tables = {}
_module.rows = {}
_module.table_id=0
_module.row_id=0

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
        'id': directives.unchanged_required,
        'headers': directives.unchanged,
        'widths': directives.unchanged,
        'title': directives.unchanged,
        'columns': directives.unchanged,
    }

    def run(self):
        node_table = nodes.table(classes=["tbl"])
        caption = None
        headers = []
        columns = None
        widths = []
        
        if 0 < len(self.arguments):
            caption = self.arguments[0]
            logger.info(f"got caption {caption}")
            if 'title' in self.options:
                node_caption = nodes.title(text=caption)
                node_table += node_caption
        else:
            caption = self.options['id']
            
        if "headers" in self.options and 0 < len(self.options['headers']):
            headers = self.options["headers"].split(", ")
            logger.info(f"found {len(headers)} entries in header")
            columns = len(headers)
        if "widths" in self.options and 0 < len(self.options['widths']):
            widths = self.options["widths"].split(", ")
            logger.info(f"found {len(widths)} entries in widths")
            columns = len(widths)
        if "columns" in self.options:
            columns = int(self.options['columns'])

        columns += 1 # todo enumeration configurable

        if columns is None:
            raise RuntimeError(f"columns could be determined from options 'headers', 'widths' or 'columns', but none seems given")
        else:
            logger.info(f"create table with {columns} columns")


        _module.row_id=0
        _module.table_id += 1

        node_tgroup = nodes.tgroup(cols=columns)
        node_table += node_tgroup
        
        # todo match headers and widths length to match together
        if 0 < len(widths):
            for width in widths:
                logger.info(f"create colspec with {int(width)} column")
                node_colspec = nodes.colspec(colwidth=int(width))
                node_tgroup += node_colspec
        else:
            for i in range(0, columns):
                logger.info(f"create colspec with {int(100/columns)} column")
                node_colspec = nodes.colspec(colwidth=int(100/columns))
                node_tgroup += node_colspec

        if 0 < len(headers):
            header_row = nodes.row()
            for header in headers:
                header_row += nodes.entry("", nodes.paragraph(text=header))
        
            node_thead = nodes.thead("",header_row)

        node_tbody = nodes.tbody()
        self.state.nested_parse(self.content,  self.content_offset, node_tbody)
        node_tgroup += node_tbody

        if 0 < len(headers):
            node_tgroup += node_thead

        tbl = self.env.get_domain('tbl')
        tbl.add_table(caption)
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
        'id': directives.unchanged_required,
    }

    def run(self):
        content_row = nodes.row(classes=["tbl", "content"])
        _module.row_id += 1
        node = nodes.entry(classes=["tbl", "content"])
        node_id = nodes.Text(f"{_module.table_id}.{_module.row_id}")
        node += node_id
        content_row += node

        self.state.nested_parse(self.content, self.content_offset, content_row)

        tbl = self.env.get_domain('tbl')
        tbl.add_row(self.options['id'])
        return [content_row]

class ColumnDirective(ObjectDescription):
    """A custom directive that describes a column in a table in the tbl domain."""

    has_content = True
    required_arguments = 0
    #option_spec = {
    #    'contains': directives.unchanged_required,
    #}
    def run(self):
        logger.info(f"adding column with content {self.content}")
        self.assert_has_content()
        node = nodes.entry(classes=["tbl", "content"])
        self.state.nested_parse(self.content,  self.content_offset, node)
        return [node]
