from pathlib import Path

import pytest
from sphinx.util import logging

logger = logging.getLogger(__name__)


@pytest.mark.parametrize("test_app", [{"buildername": "html", "srcdir": "doc_test/doc_short_example"}], indirect=True)
def test_doc_short_example(test_app):
    app = test_app
    app.build()
    html = Path(app.outdir, "index.html").read_text()

    assert "Example for a simple table" in html

    assert "This is also shown" in html

    assert "First simple table" not in html
