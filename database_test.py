# coding=utf-8
from datetime import datetime
import sqlite3
conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()
cur.execute('PRAGMA  table_info(MainGate_user)')
def sqlite3_test():
    print(cur.fetchall())
    cur.execute('select * from MainGate_user;')
    result = cur.fetchall()
    # cur.execute('insert into MainGate_user (account,password,create_time,email,login_time) '
    #             'values("common", 123456,\'{}\',"test@test.com",\'{}\');'.format(datetime.now(), datetime.now()))
    # conn.commit()
    print(result)
# test code

# nums = [2, 3, 1, 1, 4]
# nums = [1, 2, 3]
nums = [2, 0, 1]
# nums = [1, 1, 1, 1]
# nums = [2, 1, 1, 1, 1]

