def from_typeid(cursor, typeID, colName):
    (val,) = generic_query_fetchone(cursor, "invTypes", colName, "typeID",
                                    typeID)
    return val


def typename_from_typeid(cursor, typeID):
    return from_typeid(cursor, typeID, "typeName")


def volume_from_typeid(cursor, typeID):
    return from_typeid(cursor, typeID, "volume")


def generic_query_fetchone(cursor, table, qcol, col, colval):
    query = "SELECT " + qcol + " FROM " + table + " WHERE " + col + "="
    if isinstance(colval, (str, bytes)):
        query += "\"" + colval + "\""
    else:
        query += str(colval)
    query += ";"
    cursor.execute(query)
    return cursor.fetchone()
