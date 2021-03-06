def op_conv(optype, colval):
    if optype is 'eq':
        return {'op': '=', 'val': colval}
    elif optype is 'contains':
        return {'op': ' LIKE ', 'val': '%'+colval+'%'}
    elif optype is 'startswith':
        return {'op': ' LIKE ', 'val': colval+'%'}


def generic_query_cursor(cursor, table, qcol_list, col=None, optype=None,
                         colval=None, n=None):
    conv = op_conv(optype, colval)
    qcols = ", ".join(qcol_list)
    if n is not None:
        top = "TOP " + str(n)
    else:
        top = ""
    query = "SELECT " + top + qcols + " FROM " + table

    if col is not None and optype is not None and colval is not None:
        query += " WHERE " + col + conv['op']
        if isinstance(colval, (str, bytes)):
            query += "\"" + conv['val'] + "\""
        else:
            query += str(conv['val'])

    query += ";"
    cursor.execute(query)
    return cursor


def generic_query_fetchone(cursor, table, qcol_list, col=None, optype=None,
                           colval=None):
    return generic_query_cursor(
        cursor, table, qcol_list, col, optype, colval
    ).fetchone()


def generic_query_fetchn(n, cursor, table, qcol_list, col=None, optype=None,
                         colval=None):
    return generic_query_cursor(
        cursor, table, qcol_list, col, optype, colval, n
    ).fetchall()


def generic_query_fetchall(cursor, table, qcol_list, col=None, optype=None,
                           colval=None):
    return generic_query_cursor(
        cursor, table, qcol_list, col, optype, colval
    ).fetchall()


def from_typeid(cursor, typeID, colNameList):
    (val,) = generic_query_fetchone(cursor, "invTypes", colNameList, "typeID",
                                    "eq", typeID)
    return val


def typename_from_typeid(cursor, typeID):
    return from_typeid(cursor, typeID, ['typeName'])


def volume_from_typeid(cursor, typeID):
    return from_typeid(cursor, typeID, ['volume'])
