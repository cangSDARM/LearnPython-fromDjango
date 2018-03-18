import pymysql
import requests

#创建链接
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='toor')
#创建元祖游标
cursor = conn.cursor()

#创建字典游标
#cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

#严禁字符串拼接作为参数!这样会sql注入!!!

#执行mysql,并返回受影响的行数
effort_row = cursor.execute("show databases")

#fetchone, fetchmany(size), fetchall返回元祖,显示execute结果
r = cursor.fetchall()
print(r)

#执行可迭代时的mysql
# L = [('女', 'a'),('男', 'b'),('女','c')]
# r = cursor.executemany('insert into student(gender, name) values(%s,%s,%s)', L)

#执行存储过程
cursor.callproc('procname', (1, 'parmeter'))
#获取执行完存储过程的参数
cursor.execute('select @_procname_parmeter1,@_procname_parmeter2,@_procname_parmeter3')
result = cursor.fetchall()

#获取最新自增ID
auto_increment = cursor.lastrowid

#移动游标cursor
#cursor.scroll(1, mode='relative')   #相对
#cursor.scroll(2,.mode='absolute')   #绝对

#提交,否则无法保存更改
conn.commit()

#关闭游标
cursor.close()
#关闭链接
conn.close()
