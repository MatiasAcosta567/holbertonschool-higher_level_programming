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
        query = ("SELECT `name` FROM `cities`\
                 WHERE `state_id` IN (SELECT `id` FROM `states`\
                 WHERE BINARY `name` = %(state)s)")
        cur.execute(query, {'state': state})
        query_rows = cur.fetchall()
        if (len(query_rows) == 0):
            print()
        else:
            for index, row in enumerate(query_rows):
                print(row[0], end="")
                if (index < len(query_rows) - 1):
                    print("", end=", ")
                else:
                    print()
        cur.close()
        conn.close()
