#!/usr/bin/env python
# coding:utf8


def singleton(cls, *args, **kwargs):
    _instances = {}

    def _singleton():
        if cls not in _instances:
            _instances[cls] = cls(*args, **kwargs)
        return _instances[cls]
    return _singleton


if __name__ == '__main__':
    @singleton
    class SingletonTest(object):
        data = 5

    SingletonTest().data = 2
