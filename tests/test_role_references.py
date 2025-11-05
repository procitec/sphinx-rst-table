from pathlib import Path

import pytest
from sphinx.util import logging

logger = logging.getLogger(__name__)
from io import StringIO

warnings = ""
out = StringIO(warnings)

import re


@pytest.mark.parametrize(
    "test_app", [{"buildername": "html", "srcdir": "doc_test/doc_role_references", "warning": out}], indirect=True
)
def test_role_references(test_app):
    app = test_app
    app.build()
    html = Path(app.outdir, "index.html").read_text()
    
    assert "Example for a simple table" in html

    assert "Could not resolve xref for" not in out.getvalue()
    
    assert "undefined label" not in out.getvalue()

    assert ' id="row-ROW_1">1.1' in html
    assert 'href="#row-ROW_1"' in html
    
    assert ' id="table-This is a table title"' in html
    assert 'href="#table-This is a table title"' in html
