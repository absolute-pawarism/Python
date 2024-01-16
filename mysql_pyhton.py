import mysql.connector
dbconfig = {'host':'127.0.0.1','user':'root', 'password':'MSCDS', 'database': 'university'}
#OPEN DATABASE CONNECTION
db=mysql.connector.connect(**dbconfig)

#prepare a cursor object using cursor() method
cursor=db.cursor()
if(cursor):
    print("connected to DB")

#drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS employee")

#create employee table
sql="""create table employee
( first_n CHAR(20) NOT NULL, last_n CHAR(20), age INT, sex CHAR(5), income FLOAT)"""

cursor.execute(sql)

sql="insert into employee(first_n, last_n, age, sex, income)\ values ('%s','%s','%d','%c,'%d')" % ('akshay','deshmukh',23,'M',100000)

try:
    #execute sql command
    cursor.execute(sql)

    #commit your changes in the database
    db.commit()
except:
    #rollback in in case there is any error
    db.rollback()

#select employee table record
sql="select * from employee where first_n like '%s'" % ('akshay')

try:
    cursor.execute(sql)
    results=cursor.fetchall()
    for row in 