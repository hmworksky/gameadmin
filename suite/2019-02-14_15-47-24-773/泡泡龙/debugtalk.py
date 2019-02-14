
from ApiManager.utils.common import DB, MyRedis			
def insert(table, values, app = "bubble"):
    # 使用ORM更新，values(字典形式{})
    # example: values {"item_num":9001,"item_type":2} 插入一条item_num等于9001，item_type等于2的数据
    db = DB(table, app)
    result = db.insert(values)
    return result
def update(table, where, values, app = "bubble"):
    # 使用ORM更新，where(字典形式{})，values（列表形式[]）
    # example:where {"delete_flag":1} values ["id","item_num"]
    db = DB(table, app)
    result = db.update(where, values)
    return result 

def count_all(table, where=None, app = "bubble"):
    # 使用ORM查询数量，where(字典形式{},也可不传则查询该表总数)
    db = DB(table, app)
    result = db.count(where)
    return result

def select(where, values, table, app = "bubble", limit=50, order_by_data=None, group_by_data=None, is_desc=True):
    # 使用ORM查询，where(字典形式{})，values（列表形式[]）
    # order_by_data:根据哪个字段排序 传递字段名
    # group_by_data: 根据哪个字段分组
    # is_desc:是否倒序，默认是倒序，想要正序则传递True
    db = DB(table, app)
    result = db.select(where, values, limit=50, order_by_data=None, group_by_data=None, is_desc=True)
    return result

def sql(sql, app = "bubble"):
    # 使用sql语句直接查询
    # example: select *  from bubble_config
    result = DB.sql(app,sql)
    return result
    
def rget(key):
    # 从缓存获取数据，传递key
    # 使用方法: ${rget(key名字)}
    return MyRedis.get(key)
  
def rset(key, value, ex):
    # 新增或修改
    # ex 过期时间
    return MyRedis.set(key, value, ex)  
    
def rdelete(key):
    # 删除key，可传递单个或正则
    # example: 40565*
    return MyRedis.delete(key)
    


