from io import StringIO
from pathlib import Path

import pytest
from sphinx.util import logging

logger = logging.getLogger(__name__)

warnings = ""
out = StringIO(warnings)


@pytest.mark.parametrize(
    "test_app", [{"buildername": "html", "srcdir": "doc_test/doc_columns_headers", "warnings": out}], indirect=True
)
def test_columns_header(test_app):
    app = test_app
    app.build()
    html = Path(app.outdir, "index.html").read_text(encoding="utf-8")

    assert "Example for a simple table" in html

    assert ('<th class="head"><p>Auto ID</p></th>') in html

    assert ('<th class="head"><p>First Column</p></th>') in html

    assert ('<th class="head"><p>Second Column</p></th>') in html

    assert "multiline column" in html
