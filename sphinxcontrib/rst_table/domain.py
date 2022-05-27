from collections import defaultdict

from sphinx.domains import Domain, Index
from sphinx.roles import XRefRole
from sphinx.util import logging
from sphinx.util.nodes import make_refnode

from sphinxcontrib.rst_table.directives import (
    ColumnDirective,
    RowDirective,
    TableDirective,
)

logger = logging.getLogger(__name__)


class TableIndex(Index):
    """A custom index that creates an table matrix."""

    name = "tbl"
    localname = "Table Index"
    shortname = "Table"

    def generate(self, docnames=None):
        content = defaultdict(list)

        # sort the list of tables in alphabetical order
        tables = self.domain.get_objects()
        tables = sorted(tables, key=lambda table: table[0])

        # generate the expected output, shown below, from the above using the
        # first letter of the recipe as a key to group thing
        #
        # name, subtype, docname, anchor, extra, qualifier, description
        for _name, dispname, typ, docname, anchor, _priority in tables:
            content[dispname[0].lower()].append((dispname, 0, docname, anchor, docname, "", typ))

        # convert the dict to the sorted list of tuples expected
        content = sorted(content.items())

        return content, True


class TblDomain(Domain):

    name = "tbl"
    label = "TBL  Sample"
    roles = {"tbl": XRefRole(), "row": XRefRole()}

    directives = {
        "tbl": TableDirective,
        "row": RowDirective,
        "col": ColumnDirective,
    }

    indices = {TableIndex}

    initial_data = {
        "tables": [],  # object list
        "rows": [],  # object list
    }

    def get_full_qualified_name(self, node):
        return "{}.{}".format("table", node.arguments[0])

    def get_objects(self):
        for obj in self.data["tables"]:
            yield (obj)
        for obj in self.data["rows"]:
            yield (obj)

    def resolve_xref(self, env, fromdocname, builder, typ, target, node, contnode):
        match = [(docname, anchor) for name, sig, typ, docname, anchor, prio in self.get_objects() if sig == target]

        if len(match) > 0:
            todocname = match[0][0]
            targ = match[0][1]

            return make_refnode(builder, fromdocname, todocname, targ, contnode, targ)
        else:
            logger.warning(f"Could not resolve xref for {target}")
            return None

    def add_table(self, signature, id):
        """Add a new table to the domain."""
        for _id in [signature, id]:
            if _id is not None:
                name = "{}.{}".format("table", _id)
                anchor = "table-{}".format(_id)

                # name, dispname, type, docname, anchor, priority
                logger.debug(f"adding referency to tables: {name}, {_id}, {anchor}")
                self.data["tables"].append((name, _id, "Table", self.env.docname, anchor, 0))

    def add_row(self, index_entry):
        """Add a new row to the domain."""
        name = "{}.{}".format("row", index_entry)
        anchor = "row-{}".format(index_entry)

        # name, dispname, type, docname, anchor, priority
        logger.debug(f"adding referency to rows: {name}, {index_entry}, {anchor}")
        self.data["rows"].append((name, index_entry, "Row", self.env.docname, anchor, 0))
