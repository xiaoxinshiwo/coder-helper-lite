# -- coding:UTF-8 --
# Author:章永新

from threading import Thread


def async_exec(f):
    def wrapper(*args, **kwargs):
        thr = Thread(target=f, args=args, kwargs=kwargs)
        thr.start()

    return wrapper
