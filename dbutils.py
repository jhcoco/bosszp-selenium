#!/usr/bin/python
# -*- coding:utf-8 -*-
# @author  : jhzhong
# @time    : 2023/11/30 17:15
# @function: the script is used to do something.
# @version : V1
"""定义 DBUtils 工具类, 封装 MySQL 数据库常用操作 API

    - 方法1(select_all): 查询所有数据
    - 方法2(select_one): 查询一条数据
    - 方法3(select_n): 查询前 n 条数据
    - 方法4(insert_data): 插入数据
    - 方法5(update_data): 更新数据
    - 方法6(delete_data): 删除数据
"""
import pymysql


class DBUtils:
    def __init__(self, host, user, password, db, port=3306, charset='utf8'):
        """
        DBUtils 初始化方法，实例化 DBUtils 类的时候会默认调用,仅调用 1 次
        """
        # 初始化操作，例如建立数据库连接等
        self.conn = pymysql.connect(host=host, user=user, password=password, db=db, port=port, charset=charset)
        # 获取游标 pymysql.cursors.DictCursor 指定返回值类型为 字典 类型
        self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)

    def select_all(self, sql, args=None):
        """
        查询所有数据
        :param sql: 查询数据的 sql
        :param args: 参数，只能是元组或者列表
        :return: 返回结果集
        """
        self.cursor.execute(sql, args)
        result = self.cursor.fetchall()
        return result

    def select_n(self, sql, n, args=None):
        """
        查询满足条件的前 n 条数据
        :param sql: 查询数据的 sql
        :param n: 查询的条数
        :param args: 参数，只能是元组或者列表
        :return: 返回结果集
        """
        self.cursor.execute(sql, args)
        result = self.cursor.fetchmany(n)
        return result

    def select_one(self, sql, args=None):
        """
        查询满足条件的第 1 条数据
        :param sql: 查询数据的 sql
        :param args: 参数，只能是元组或者列表
        :return: 返回结果集
        """
        self.cursor.execute(sql, args)
        result = self.cursor.fetchone()
        return result

    def insert_data(self, sql, args=None):
        """
        插入数据
        :param sql: 插入数据的 sql
        :param args: 参数，只能是元组或者列表
        :return: 返回受影响的行数
        """
        self.cursor.execute(sql, args)
        self.conn.commit()
        return self.cursor.rowcount

    def update_data(self, sql, args=None):
        """
        更新数据
        :param sql: 更新数据的 sql
        :param args: 参数，只能是元组或者列表
        :return: 返回受影响的行数
        """
        self.cursor.execute(sql, args)
        self.conn.commit()
        return self.cursor.rowcount

    def delete_data(self, sql, args=None):
        """
        删除数据
        :param sql: 删除数据的 sql
        :param args: 参数，只能是元组或者列表
        :return: 返回受影响的行数
        """
        self.cursor.execute(sql, args)
        self.conn.commit()
        return self.cursor.rowcount

    def close(self):
        """
        关闭数据库连接
        """
        self.cursor.close()
        self.conn.close()




# 定义 main 函数
if __name__ == '__main__':
    # 实例化 DBUtils
    db = DBUtils('localhost', 'root', '123456', 'spring')

    # 测试查询所有数据
    """ret = db.select_all("select * from t_user")
    for r in ret:
        print(r)"""

    # 测试查询前 n 条数据
    """ret = db.select_n("select * from t_user", 3)
    for r in ret:
        print(r)"""

    # 测试查询 1 条数据
    """ret = db.select_one("select * from t_user where username = %s and password = %s", ['admin', 'admin'])
    print(ret)"""

    # 测试插入数据
    """rows = db.insert_data("insert into t_user(username,password) values(%s,%s)", ['李玉梅', '000000'])
    print(rows)"""

    # 测试更新数据
    """rows = db.update_data("update t_user set password = %s where username = %s", ['123456', '李玉'])
    print(rows)"""

    # 测试删除数据
    """rows = db.delete_data("delete from t_user where username = %s", ['李玉梅'])
    print(rows)"""

    # 关闭数据库连接
    db.close()