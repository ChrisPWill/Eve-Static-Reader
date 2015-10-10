def name_from_typeid(cursor, typeID):
    return generic_query("invTypes", "typeName", "typeID", typeID)


def vol_from_typeid(cursor, typeID):
    return generic_query("invTypes", "volume", "typeID", typeID)


def generic_query(cursor, table, qcol, col, colval):
    query = "SELECT " + qcol + " FROM " + table + " WHERE " + col + "="
    if isinstance(colval, (str, bytes)):
        query += "\"" + colval + "\""
    else:
        query += str(colval)
    query += ";"
    cursor.execute(query)
    return cursor.fetchall()
