from pathlib import Path

import pytest
from sphinx.util import logging

logger = logging.getLogger(__name__)
from io import StringIO

warnings = ""
out = StringIO(warnings)

import re


@pytest.mark.parametrize(
    "test_app", [{"buildername": "html", "srcdir": "doc_test/doc_columns_rowspan", "warnings": out}], indirect=True
)
def test_columns_rowspan(test_app):
    app = test_app
    app.build()
    html = Path(app.outdir, "index.html").read_text()

    assert "Example for a rowspan table" in html

    assert( '<th class="head"><p>Auto ID</p></th>') in html

    assert( '<th class="head"><p>First Column</p></th>') in html

    assert( '<th class="head"><p>Second Column</p></th>') in html

    assert( 'rowspan="2"' ) in html

    assert( "This should be spanned</p></td>\n</tr>" ) in html

    assert( '<td class="tbl-col"><p>r3c1</p></td>\n<td class="tbl-col"><p>r3c2</p></td>' ) in html

