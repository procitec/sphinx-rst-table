from collections import defaultdict

from sphinxcontrib.rst_table.directives import TableDirective, RowDirective, ColumnDirective
from sphinx.domains import Domain, Index
from sphinx.roles import XRefRole
from sphinx.util.nodes import make_refnode
from sphinx.util import logging
logger = logging.getLogger(__name__)


class TableIndex(Index):
    """A custom index that creates an table matrix."""

    name = 'tbl'
    localname = 'Table Index'
    shortname = 'Table'

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
            content[dispname[0].lower()].append(
                (dispname, 0, docname, anchor, docname, '', typ))

        # convert the dict to the sorted list of tuples expected
        content = sorted(content.items())

        return content, True


class TblDomain(Domain):

    name = 'tbl'
    label = 'TBL  Sample'
    roles = {
        'tbl': XRefRole(),
        'row': XRefRole()
    }
    
    directives = {
        'tbl': TableDirective,
        'row': RowDirective,
        'column': ColumnDirective,
    }
    
    indices = {
        TableIndex
    }
    
    initial_data = {
        'tables': [],  # object list
        'rows': [],  # object list
    }
    
    def get_full_qualified_name(self, node):
        return '{}.{}'.format('table', node.arguments[0])

    def get_objects(self):
        for obj in self.data['tables']:
            yield(obj)

    def resolve_xref(self, env, fromdocname, builder, typ, target, node,
                     contnode):
        match = [(docname, anchor)
                 for name, sig, typ, docname, anchor, prio
                 in self.get_objects() if sig == target]

        if len(match) > 0:
            todocname = match[0][0]
            targ = match[0][1]

            return make_refnode(builder, fromdocname, todocname, targ,
                                contnode, targ)
        else:
            logger.warning(f"Could not resolve xref for {target}" )
            return None

    def add_table(self, signature):
        """Add a new table to the domain."""
        name = '{}.{}'.format('table', signature)
        anchor = 'table-{}'.format(signature)

        # name, dispname, type, docname, anchor, priority
        self.data['tables'].append(
            (name, signature, 'Table', self.env.docname, anchor, 0))

    def add_row(self, signature):
        """Add a new row to the domain."""
        name = '{}.{}'.format('row', signature)
        anchor = 'row-{}'.format(signature)

        # name, dispname, type, docname, anchor, priority
        self.data['rows'].append(
            (name, signature, 'Row', self.env.docname, anchor, 0))