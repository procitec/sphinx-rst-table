from pathlib import Path

from sphinx.errors import ExtensionError

import pytest

from sphinx.util import logging
logger = logging.getLogger(__name__)

@pytest.mark.parametrize("test_app", [{"buildername": "html", "srcdir": "doc_test/doc_error_columns"}], indirect=True)
def test_doc_error_columns(test_app):
    app = test_app
    try:
        app.build()
        html = Path(app.outdir, "index.html").read_text()
        assert ( False ) # this should not be reached

    except ExtensionError as e:
        assert (
            "could not determine number of columns from header or widths options. 'columns' options must be given" in str(e)
        )
