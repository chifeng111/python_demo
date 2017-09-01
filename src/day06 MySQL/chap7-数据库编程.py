# coding: utf-8
import MySQLdb

if __name__ == '__main__':
    # 打开数据库连接
    db = MySQLdb.connect(host="119.29.16.160", user="root",
                         passwd="lzh12345", db="chap3", charset="utf8")

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # 使用execute方法执行SQL语句
    cursor.execute("SELECT VERSION()")

    # 使用 fetchone() 方法获取一条数据库。
    data = cursor.fetchone()

    print("Database version : %s " % data)

    # 关闭数据库连接
    db.close()
