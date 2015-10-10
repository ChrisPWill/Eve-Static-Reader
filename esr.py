import configparser
import sqlite3

from os.path import join

config = configparser.ConfigParser()
config.read('settings.ini')
db_loc = join(config['DEFAULT']['db_dir'],
              config['DEFAULT']['db_filename'])
use_mem = config['DEFAULT']['use_mem']
if "yes" in use_mem:
    file_conn = sqlite3.connect(db_loc)

    def tf(x):
        return str(x, 'utf-8', 'ignore')

    file_conn.text_factory = tf
    conn = sqlite3.connect(':memory:')

    query = "".join(line for line in file_conn.iterdump())
    conn.executescript(query)
else:
    conn = sqlite3.connect(db_loc)


def name_from_typeid(typeID):
    return generic_query("invTypes", "typeName", "typeID", typeID)


def vol_from_typeid(typeID):
    return generic_query("invTypes", "volume", "typeID", typeID)


def generic_query(table, qcol, col, colval):
    cursor = __cursor()
    query = "SELECT " + qcol + " FROM " + table + " WHERE " + col + "="
    if isinstance(colval, (str, bytes)):
        query += "\"" + colval + "\""
    else:
        query += str(colval)
    query += ";"
    cursor.execute(query)
    return cursor.fetchall()


def printtables():
    print(__tablelist())


def __cursor():
    return conn.cursor()


def __tablelist():
    cursor = __cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    return cursor.fetchall()
