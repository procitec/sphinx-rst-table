pybabel extract --output=sphinxcontrib/rst_table/locales/sphinxcontrib.rst_table.pot sphinxcontrib/rst_table
pybabel init --input-file=sphinxcontrib/rst_table/locales/sphinxcontrib.rst_table.pot --domain=sphinxcontrib.rst_table --output-dir=sphinxcontrib/rst_table/locales --locale=de_DE
pybabel init --input-file=sphinxcontrib/rst_table/locales/sphinxcontrib.rst_table.pot --domain=sphinxcontrib.rst_table --output-dir=sphinxcontrib/rst_table/locales --locale=en_US
pybabel update --input-file=sphinxcontrib/rst_table/locales/sphinxcontrib.rst_table.pot --domain=sphinxcontrib.rst_table --output-dir=sphinxcontrib/rst_table/locales
pybabel compile --directory=sphinxcontrib/rst_table/locales --domain=sphinxcontrib.rst_table
