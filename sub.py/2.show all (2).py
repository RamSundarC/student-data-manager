import mysql.connector

db=mysql.connector.connect(
	host='localhost',
	user='root',
	password='pappy',
	database='visualizer'
	)

mycursor=db.cursor()


options=int(input('Select Operation:\n1.To Get Data about a student\n2.To view list of data\n3.To Insert data\n4.To update data\n5.To delete data'))

if options==2:
    sql='SELECT * from home'
    mycursor.execute(sql)
    for a in mycursor:
        print(a)
