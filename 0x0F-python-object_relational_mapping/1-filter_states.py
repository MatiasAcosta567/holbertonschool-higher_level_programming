#!/usr/bin/python3
"""Connect to MySQL Database"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    """Main Entry"""
    if (len(argv) == 4):
        username = argv[1]
        password = argv[2]
        dbname = argv[3]
        conn = MySQLdb.connect(host="localhost", port=3306,
                               user=username, passwd=password,
                               db=dbname, charset="utf8")
        cur = conn.cursor()
        cur.execute(
            'SELECT * FROM `states`ORDER BY `id` ASC')
        query_rows = cur.fetchall()
        for row in query_rows:
            if (row[1][0] == 'N'):
                print(row)
        cur.close()
        conn.close()
