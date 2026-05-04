import os
from importlib.metadata import PackageNotFoundError
from importlib.metadata import version as package_version

from sphinx.util import logging

from sphinx_rst_table.domain import MESSAGE_CATALOG_NAME, TblDomain

LOG = logging.getLogger(__name__)
PACKAGE_NAME = "sphinx-rst-table"


def get_extension_version() -> str:
    """Return the installed package version from package metadata.

    The version is maintained in ``pyproject.toml`` only. When the package is
    installed, that value is exposed through Python package metadata and used
    by Sphinx in ``setup()``. The fallback is only for direct source-tree usage
    without an installed distribution.
    """
    try:
        return package_version(PACKAGE_NAME)
    except PackageNotFoundError:
        return "0+unknown"


def setup(app):
    app.add_config_value("rst_table_autonumber", False, "html")
    app.add_config_value("rst_table_autonumber_reset_on_table", True, "html")
    app.add_domain(TblDomain)

    package_dir = os.path.abspath(os.path.dirname(__file__))
    locale_dir = os.path.join(package_dir, "locales")
    LOG.debug("using locale dir %s", locale_dir)
    app.add_message_catalog(MESSAGE_CATALOG_NAME, locale_dir)

    return {
        "version": get_extension_version(),
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
