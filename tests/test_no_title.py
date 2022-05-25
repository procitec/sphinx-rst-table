from pathlib import Path

import pytest

from sphinx.util import logging
logger = logging.getLogger(__name__)
from io import StringIO 
warnings = ""
out = StringIO(warnings)

@pytest.mark.parametrize("test_app", [{"buildername": "html", "srcdir": "doc_test/doc_no_title", "warning": out}], indirect=True)
def test_no_title(test_app):
    app = test_app
    app.build()
    html = Path(app.outdir, "index.html").read_text()
    
    assert (
        'Example for a simple table' in html
    )
    
    assert (
        'index.rst:4: ERROR: Error in "tbl:tbl" directive:' in out.getvalue()
    )

    assert(
        'multiline column' not in html
    )
