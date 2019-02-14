
def D(connects=None, sql=None, app=None, table=None, type=None, **kwargs):
    from ApiManager.utils.common import DB
    if connects and sql:
        return DB.sql(connects,sql)
    elif table:
        d = DB(table=table, app=app)
        func_list = {
            "select": d.select(**kwargs),
            "insert": d.insert(**kwargs),
            "update": d.update(**kwargs),
            "count": d.count(**kwargs)
        }
        result = func_list.get(type, "select")
        return result

    # debugtalk.py
def hello():
    return 2
