
.. From here shared with index.rst of docs folder. #SHARED_CONTENT

sphinxcontrib-rst-table
=======================

Sphinx extension to create tables with normal Sphin/ReST directives

`sphinxcontrib-rst-table <https://github.com/procitec/sphinxcontrib-rst-table>`_ is a Sphinx extension to generate table output with ReST directives.

These tables are seamlessly integrated in the output of your specific builder, with limitations due to
the specific builder.

Motivation
----------

During work with Sphinx tables seems always a bit difficult to handle, but for most use cases some helpful extensions
are available. So if you just want to display table data the normal `list-table <https://docutils.sourceforge.io/docs/ref/rst/directives.html#list-table>`_
or `csv-table <https://docutils.sourceforge.io/docs/ref/rst/directives.html#csv-table>`_ directives 
are very helpful. Also some other extension like `sphinxcontrib.datatemplates <https://github.com/sphinx-contrib/datatemplates>`_

.. ` <>`_

But some use cases are still not handled or only availabe with the ReST `grid-tables <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#grid-tables>`_.

These are for example:

    * Inserting images in your table cells
    * Multi-line cell data
    * Use of other sphinx directives in your cell content
    * Auto-number rows inbetween tables and over different tables
    * Cross referencing of rows cells in your table

This was the point we deciced to make an extension for it.


Introduction
-------------

``sphinxcontrib-rst-table`` uses normal directives from the ``tbl`` (table) domain to add tables, rows and cells

    .. code-block:: rst
    
        .. tbl:tbl:: The simplest table
            :columns: 2

            .. tbl:row::
                
                .. tbl:col:: This is a colum with *italic* content
                
                .. tbl:col:: This is the second colum


The directive ``tbl:tbl`` inserts a table. A title must be given for referencing, but is not shown until ``:title:`` option is set.
The directive also requires a ``:columns:`` option if there are now ``:headers:`` or ``:widths:`` set as option to determine the number
of cells. 


A new row is inserted with ``tbl:row``. The directive has no title. Optional a ``:id:`` option could be set for referencing the row from other cells.

The column content is inserted with the ``tbl:row`` directive.


Documentation for the directives is in :ref:`directives`.


Installation
------------

Currently the extension is not builded and provides as whl. But you can use it by downloading and

* Adding the download folder to your PYTHONPATH environment variable
* Build the package by calling :code:`python setup.py build`

