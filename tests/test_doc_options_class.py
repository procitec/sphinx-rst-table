from pathlib import Path

import pytest
from sphinx.util import logging

logger = logging.getLogger(__name__)


@pytest.mark.parametrize("test_app", [{"buildername": "html", "srcdir": "doc_test/doc_options_class"}], indirect=True)
def test_doc_options_class(test_app):
    app = test_app
    app.build()
    html = Path(app.outdir, "index.html").read_text()

    assert "table-class" in html
    assert "row-class" in html
    assert "col-class" in html

    assert "col-class" in html
    assert html.count("col-class") == 2
