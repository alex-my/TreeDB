#!/usr/bin/env python
# coding:utf8
from mysql.connector import errors
from TreeDB.common.Singleton import singleton
from TreeDB.core.DBPool import DBPool


@singleton
class DBPoolManager(object):
    def __init__(self):
        self._pools = {}

    def register_pool(self, pool_name=None, pool_size=5, **db_config):
        if pool_name is None:
            raise errors.PoolError(
                'pool_name can not be none')
        pool = DBPool(pool_name=pool_name, pool_size=pool_size, **db_config)
        if not pool or not pool.init_connection():
            return False
        self._pools[pool_name] = pool
        return True

    def get_pool(self, pool_name):
        if pool_name is None:
            raise errors.PoolError(
                'pool_name can not be none')
        return self._pools.get(pool_name)

    def drop_pool(self, pool_name):
        if pool_name is None:
            raise errors.PoolError(
                'pool_name can not be none')
        if pool_name in self._pools:
            del self._pools[pool_name]


if __name__ == '__main__':
    db_config = {
        'user': 'root',
        'password': '123456',
        'host': '127.0.0.1',
        'port': 3306,
        'database': 'learn_server'
    }
    flag = DBPoolManager().register_pool(pool_name='test_learn_server',
                                         pool_size=3,
                                         **db_config)
    if not flag:
        print 'register pool failed'
        exit(1)
    pool = DBPoolManager().get_pool('test_learn_server')
    if not pool:
        print 'pool is none'
        exit(1)
    print 'running success'
