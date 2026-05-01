from io import StringIO
from pathlib import Path

import pytest

warnings = ""
out = StringIO(warnings)


@pytest.mark.parametrize(
    "test_app", [{"buildername": "html", "srcdir": "doc_test/doc_columns_header_rows", "warnings": out}], indirect=True
)
def test_columns_header_rows(test_app):
    app = test_app
    app.build()
    html = Path(app.outdir, "index.html").read_text(encoding="utf-8")

    assert "Example for a simple table" in html

    assert ('<th class="head"><p>Auto ID</p></th>') in html

    assert ('<th class="head"><p>First Column</p></th>') in html

    assert ('<th class="head"><p>Second Column</p></th>') in html

    assert ('<td class="tbl-col"><p>This is a colum with <em>italic</em> content</p></td>') in html

    assert "multiline column" in html
