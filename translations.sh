pybabel extract --output=sphinx_rst_table/locales/sphinx_rst_table.pot sphinx_rst_table
pybabel init --input-file=sphinx_rst_table/locales/sphinx_rst_table.pot --domain=sphinx_rst_table --output-dir=sphinx_rst_table/locales --locale=de_DE
pybabel init --input-file=sphinx_rst_table/locales/sphinx_rst_table.pot --domain=sphinx_rst_table --output-dir=sphinx_rst_table/locales --locale=en_US
pybabel update --input-file=sphinx_rst_table/locales/sphinx_rst_table.pot --domain=sphinx_rst_table --output-dir=sphinx_rst_table/locales
pybabel compile --directory=sphinx_rst_table/locales --domain=sphinx_rst_table
