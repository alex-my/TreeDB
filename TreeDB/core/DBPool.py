#!/usr/bin/env python
# coding:utf8
import mysql.connector


class DBPool(object):
    def __init__(self, pool_name=None, pool_size=5, **db_config):
        self._pool_name = pool_name
        self._pool_size = pool_size
        self._db_config = db_config

    def init_connection(self):
        try:
            self._pool = mysql.connector.pooling.MySQLConnectionPool(
                pool_name=self._pool_name,
                pool_size=self._pool_size,
                **self._db_config)
            return True
        except mysql.connector.PoolError as err:
            print 'Error init_connection: {}'.format(err)
            return False

    def close_connection(self, cnx):
        """cnx is subclass of MySQLConnection"""
        if cnx is None:
            return
        self.fill_connection(cnx)

    def fill_connection(self, cnx):
        """cnx is subclass of MySQLConnection"""
        try:
            self._pool.add_connection(cnx)
        except mysql.connector.PoolError as err:
            print 'Error fill_connection: {}'.format(err)
            cnx.close()

    def get_connection(self):
        """return PooledMySQLConnection instance"""
        return self._pool.get_connection() if self._pool else None

    def set_config(self, **kwargs):
        self._pool.set_config(**kwargs)

if __name__ == '__main__':
    pool = DBPool(user='root',
                  password='123456',
                  host='127.0.0.1',
                  port=3306,
                  database='learn_server')
    if not pool.init_connection():
        print 'pool init connection failed.'
        exit(1)
    pcnx = pool.get_connection()
    pcnx.close()    # will add the connection back to the pool
