def registar(dbname):
    data = {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_game_{}'.format(dbname),
        'USER': 'game_dev',
        'PASSWORD': 'game_dev123',
        'HOST': '21.58.201.44',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'charset': 'utf8',
        }
    }
    return data
