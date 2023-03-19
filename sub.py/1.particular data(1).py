import pandas as pd
import mysql.connector

db=mysql.connector.connect(
	host='localhost',
	user='root',
	password='pappy',
	database='visualizer'
	)

mycursor=db.cursor()

options=int(input('Select Operation:\n1.To Get Data about a student\n2.To view list of data\n3.To Insert data\n4.To update data\n5.To delete data'))

if options==1:
    no=int(input('Enter Roll_No to view the data:'))

    mycursor.execute('Select * from home where roll_no=%s',(no,))  
    result=mycursor.fetchone()

    if result is not None:
        print("One Data Found")
        for m in result:
            print(m)
    else:
       print("Something went wrong")




  


 




   