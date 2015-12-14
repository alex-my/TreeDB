#!/usr/bin/env python
# coding:utf8
import mysql.connector
from core.DBPoolManager import DBPoolManager


class DB(object):
    def __init__(self):
        self._cnx = None
        self._cursor = None

    def open(self, pool_name):
        pool = DBPoolManager().get_pool(pool_name)
        if pool:
            self._cnx = pool.get_connection()
            if not self._cnx:
                raise Exception('cnx get failed, database %s' % pool_name)
            self._cursor = self._cnx.cursor(buffered=True)
        else:
            raise Exception('open database %s failed' % pool_name)

    def close(self):
        if self._cursor:
            self._cursor.close()
        if self._cnx:
            self._cnx.close()

    def next_record(self):
        self._cursor.nextset()

    def execute(self, sql):
        try:
            return self._cursor.execute(sql)
        except mysql.connector.Error as err:
            print 'execute sql: {0}  failed, error: {1} '.format(sql, err)
            return -1

    def insert(self, table_name, data):
        for key in data:
            data[key] = "'" + str(data[key]) + "'"
        keys = ','.join(data.keys())
        values = ','.join(data.values())
        sql = "insert into " + table_name + " (" + keys + ") values (" + values + ")"
        return self.execute(sql)

    def get_insert_id(self):
        return self._cursor.lastrowid

    def replace(self, table_name, data):
        for key in data:
            data[key] = "'" + str(data[key]) + "'"
        keys = ','.join(data.keys())
        values = ','.join(data.values())
        sql = "replace into " + table_name + " (" + keys + ") values (" + values + ")"
        return self.execute(sql)

    def update(self, table_name, data, where, where_flag='=', where_conn='and'):
        for key in data:
            data[key] = "'" + str(data[key]) + "'"
        for key in where:
            where[key] = "'" + str(where[key]) + "'"
        data_sql = ','.join([str(k) + " = " + str(v) for k, v in data.items()])
        where_sql = (' %s ' % where_conn).join([str(k) + ' ' + where_flag + ' ' + str(v) for k, v in where.items()])
        sql = "update " + table_name + " set " + data_sql + " where " + where_sql
        return self.execute(sql)

    def delete(self, table_name, where, where_flag='=', where_conn='and'):
        for key in where:
            where[key] = "'" + str(where[key]) + "'"
        where_sql = (' %s ' % where_conn).join([str(k) + ' ' + where_flag + ' ' + str(v) for k, v in where.items()])
        sql = "delete from " + table_name + " where " + where_sql
        print 'delete sql: ', sql
        return self.execute(sql)

    def select(self, sql):
        self.execute(sql)
        result = self._cursor.fetchall()
        desc = self._cursor.description

        def analyze(r):
            _list = []
            for i in range(0, len(r)):
                _list[desc[i][0]] = str(r[i])
            return _list

        return [analyze(d) for d in result]

    def select_one(self, sql):
        self.execute(sql)
        return self._cursor.fetchone()

    def commit(self):
        self._cnx.commit()


if __name__ == '__main__':
    import time
    db_config = {
        'user': 'root',
        'password': '123456',
        'host': '127.0.0.1',
        'port': 3306,
        'database': 'learn_server',
        'autocommit': False
    }
    pool_name = 'test_learn_server'
    flag = DBPoolManager().registe_pool(pool_name=pool_name,
                                        pool_size=5,
                                        **db_config)
    if not flag:
        raise Exception('regist pool failed.')
    db = DB()
    db.open(pool_name)
    t = int(time.time())
    # test insert, get_insert_id
    role_infomation = {
            'account_id': 1,
            'channel_id': 1,
            'name': str(t)
        }
    db.insert('role', role_infomation)
    role_id = db.get_insert_id()
    # test replace
    replace_infomation = {
            'role_id': role_id - 1 if role_id > 1 else 1,
            'account_id': 2,
            'channel_id': 2,
            'name': str(t + 1)
        }
    db.replace('role', replace_infomation)
    # test update
    db.update('role', {'account_id': 4}, {'role_id': 5}, where_flag='<')
    # test delete
    db.delete('role', {'role_id': 5, 'account_id': 1}, where_flag='<', where_conn='or')
    # test select
    print db.select("select * from 'role'")
    print db.select_one("select * from 'role' where 'id' = 10")
    db.commit()
