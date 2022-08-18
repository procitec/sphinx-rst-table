from pathlib import Path

import pytest
from sphinx.util import logging

logger = logging.getLogger(__name__)


@pytest.mark.parametrize("test_app", [{"buildername": "html", "srcdir": "doc_test/doc_table_index_de"}], indirect=True)
def test_doc_example(test_app):
    app = test_app
    app.build()
    html = Path(app.outdir, "index.html").read_text()

    assert "Einfache Tabelle" in html

    assert "mehrzeilige Zelle" in html

    assert "1.1" in html  # from autonumber config value

    assert 'title="Stichwortverzeichnis"' in html # to ensure german is set as language

    assert "tbl-tbl.html" in html

    assert "Tabellen Index" in html

    html = Path( app.outdir, "tbl-tbl.html").read_text()

    assert 'title="Tabellen Index"' in html
