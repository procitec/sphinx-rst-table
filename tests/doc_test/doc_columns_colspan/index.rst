Example for a colspan table
===========================

.. tbl:tbl:: First colspan table
    :headers: Auto ID, First Column,Second Column

    .. tbl:row::
        
        .. tbl:col::
               
            r1c1

        .. tbl:col::

            r1c2

    .. tbl:row::

        .. tbl:col::
            :colspan: 2

            This should be spanned

    .. tbl:row::

        .. tbl:col::

            r3c1

        .. tbl:col::

            r3c2
