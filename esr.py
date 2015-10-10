import configparser
import sqlite3

from os.path import join


class ESR:
    def printtables(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        print(cursor.fetchall())

    def __init__(self):
        config = configparser.ConfigParser()
        config.read('settings.ini')
        db_loc = join(config['DEFAULT']['db_dir'],
                      config['DEFAULT']['db_filename'])
        use_mem = config['DEFAULT']['use_mem']
        if "yes" in use_mem:
            file_conn = sqlite3.connect(db_loc)

            def tf(x): str(x, 'latin1')

            file_conn.text_factory = tf
            self.conn = sqlite3.connect(':memory:')
            tables = config['DEFAULT']['db_tables'].split()
            for table_name in tables:
                for line in file_conn.iterdump():
                    if table_name in line:
                        query = line
                        break
                self.conn.executescript(query)
        else:
            self.conn = sqlite3.connect(db_loc)
