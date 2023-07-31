from pathlib import Path

import pytest
from sphinx.util import logging

logger = logging.getLogger(__name__)


@pytest.mark.parametrize("test_app", [{"buildername": "html", "srcdir": "doc_test/doc_no_autonumber"}], indirect=True)
def test_doc_no_autonumber(test_app):
    app = test_app
    app.build()
    html = Path(app.outdir, "index.html").read_text()

    assert "Example for a simple table" in html

    assert "multiline column" in html

    assert ">1.1</td>" not in html  # from autonumber config value
