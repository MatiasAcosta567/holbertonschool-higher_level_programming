#!/usr/bin/python3
"""Connect to MySQL Database"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    if (len(argv) == 5):
        username = argv[1]
        password = argv[2]
        dbname = argv[3]
        state = argv[4]
        conn = MySQLdb.connect(host="localhost", port=3306,
                               user=username, passwd=password,
                               db=dbname, charset="utf8")
        cur = conn.cursor()
        query = "SELECT * FROM `states` WHERE\
            BINARY `name` = %(state)s ORDER BY id ASC"
        cur.execute(query, {'state': state})
        query_rows = cur.fetchall()
        for row in query_rows:
            print(row)
        cur.close()
        conn.close()
