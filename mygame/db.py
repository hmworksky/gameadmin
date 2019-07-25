import sys
WIN_FLAG = True if 'win' in sys.platform else False
myname = 3


def registar(dbname):
    data = {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_game_{}'.format(dbname) if not WIN_FLAG else 'gameadmin',
        'USER': 'game_dev' if not WIN_FLAG else 'root',
        'PASSWORD': 'game_dev123' if not WIN_FLAG else 'test1324',
        'HOST': '21.58.201.44' if not WIN_FLAG else '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'charset': 'utf8',
        }
    }
    return data


def auto(dbname):
    data = {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'auto_{}'.format(dbname),
        'USER': 'game_dev' if not WIN_FLAG else 'root',
        'PASSWORD': 'game_dev123' if not WIN_FLAG else 'test1324',
        'HOST': '21.58.201.44' if not WIN_FLAG else '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'charset': 'utf8',
        }
    }
    return data

