#!/usr/bin/python3
''' <TODO> docstring of the module for the relevant question '''
from MySQLdb import connect
import sys

if __name__ == '__main__':
    host = 'localhost'
    user, passwd, dbname, name = sys.argv[1:5]

    db = connect(host=host, user=user, passwd=passwd, db=dbname)
    cur = db.cursor()

    cur.execute('select * from states where name="{0}" order by id;'
                .format(name))
    for row in cur.fetchall():
        if row[1] == name:
            print(row)
    cur.close()
    db.close()
