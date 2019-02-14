import sys
import os
sys.path.append('D:\project\HttpRunnerManager')
from ApiManager.utils.common import DB	
def in_file(msg):
    with open('mylog.log', 'w+') as f:
        f.write(msg)
def insert(table, values, app = "bubble"):
    db = DB(table, app)
    result = db.insert(values)
    return result 

def update(table, where, values, app = "bubble"):
    db = DB(table, app)
    result = db.update(where, values)
    return result 

def count(table, where, app = "bubble"):
    in_file("###进入count函数了###")
    db = DB(table, app)
    result = db.count(where)
    return result

def select(where, values, table, app = "bubble", limit=50, order_by_data=None, group_by_data=None, is_desc=True):
    db = DB(table, app)
    result = db.select(where, values, limit=50, order_by_data=None, group_by_data=None, is_desc=True)
    return result

def sql(sql, app = "bubble"):
    result = DB.sql(app,sql)
    return result
