"""Pytest conftest module containing common test configuration and fixtures."""

import shutil
from pathlib import Path

import pytest

pytest_plugins = "sphinx.testing.fixtures"


def copy_srcdir_to_tmpdir(srcdir: str | Path, tmp: str | Path) -> Path:
    src_path = Path(__file__).parent.resolve() / srcdir
    tmp_root = Path(tmp) / src_path.name

    shutil.copytree(src_path, tmp_root)

    return tmp_root


@pytest.fixture(scope="function")
def test_app(make_app, sphinx_test_tempdir, request):
    builder_params = request.param

    srcdir = builder_params.get("srcdir", None)
    src_dir = copy_srcdir_to_tmpdir(srcdir, sphinx_test_tempdir)

    external_data_dir = builder_params.get("datadir", None)
    if external_data_dir is not None:
        copy_srcdir_to_tmpdir(external_data_dir, sphinx_test_tempdir)

    app = make_app(
        buildername=builder_params.get("buildername", "html"),
        srcdir=src_dir,
        freshenv=builder_params.get("freshenv", None),
        confoverrides=builder_params.get("confoverrides", None),
        status=builder_params.get("status", None),
        warning=builder_params.get("warning", None),
        tags=builder_params.get("tags", None),
        docutilsconf=builder_params.get("docutilsconf", None),
        parallel=builder_params.get("parallel", 0),
    )

    yield app
