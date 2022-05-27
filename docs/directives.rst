.. _directives:

Directives
==========


.. rst:directive:: :tbl:table

    A table is added to the document with the directive `tbl:tbl`:

    .. code-block:: rst

        .. :tbl:tbl: Title of the Table

    The title is required (e.g. for references). The options for the directive are:


    .. rubric:: Options

    .. rst:directive:option:: title
        :type: str
        
        If set, the title will be shown in output. Default is not to show the table title. The title
        will be shown on top of the table. This is currently not configurable.

    .. rst:directive:option:: columns
        :type: int
        
        Number of columns. This number must only be given if not ``:headers:`` or ``:widths:`` option is used.
        The given number of columns should be set **without** considering the ``autonumber`` column.

    .. rst:directive:option:: headers
        :type: [int]
        
        The header columns text. The string must be comma separated (', ') and must not include quoatation marks
        The given number of columns should be set **with** considering the ``autonumber`` column to give this column
        also an header entry.

    .. rst:directive:option:: widths
        :type: [int]
        
        The columns widths in percentages. The string must be comma separated (', ').
        The given number of widths should be set **with** considering the ``autonumber`` column to give this column
        also an width.

    .. rst:directive:option:: class
        :type: str

        The class name for html output to use in css files. By default 'tbl' is added.


.. rst:directive:: :tbl:row

A row is added to the document with the directive `tbl:row`.
The directive requires no arguments.

    .. rubric:: Options

    .. rst:directive:option:: id
        :type: str

        An additional id the row could be referenced.

    .. rst:directive:option:: class
        :type: str
        
        The class name for html output to use in css files. By default 'tbl-row' is added.

.. rst:directive:: :tbl:col

    A column is added to the document with the directive `tbl:col`.
    The directive requires no arguments, but the content could be given as argument (direct content after the directive on the same line)
    or as a content block. The node is parsed recursivly for further Sphinx content.

    .. rubric:: Options

    .. rst:directive:option:: class
        :type: str
        
        The class name for html output to use in css files. By default 'tbl-row' is added.
