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

if options==5:
    choice=int(input('Enter Roll_No to delete the data'))

    mycursor.execute('DELETE FROM home WHERE roll_no=%s',(choice,))

    db.commit()
    print('Record was deleted successfully')