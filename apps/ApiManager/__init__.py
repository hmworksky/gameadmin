import platform

separator = '\\' if platform.system() == 'Windows' else '/'
__all__ = ['views', 'tasks', 'models', 'machines', 'managers', 'apps', 'admin', 'utils', 'templatetags',
           'migrations']
