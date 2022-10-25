Example for a rowspan table
===========================

.. tbl:tbl:: First rowspan table
    :headers: Auto ID, First Column,Second Column

    .. tbl:row::
        
        .. tbl:col::
               
            r1c1

        .. tbl:col::
            :rowspan: 2

            This should be spanned

    .. tbl:row::

        .. tbl:col::

            rc2c1


    .. tbl:row::

        .. tbl:col::

            r3c1

        .. tbl:col::

            r3c2
