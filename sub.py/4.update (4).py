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
if options==4:
    select_1=int(input('What do you want to update in the table?:\n1.Name\n2.Mark1\n3.Mark2\n4.Mark3\n5.Mark4\n6.Mark5:'))
    if select_1==1:
        select_2=int(input("Enter Roll_no modify:"))
        changes=input("Enter New Name:")
        sql='Update home SET name=%s where roll_no=%s'
        mycursor.execute(sql,(changes,select_2))
        db.commit()
        print("Successfully modified")
  
    elif select_1==2:
        select_2=int(input("Enter Roll_no modify:"))
        changes=int(input('Enter New Mark1:'))
        sql='Update home SET mark1=%s where roll_no=%s'
        mycursor.execute(sql,(changes,select_2))
        db.commit()
        print("Successfully modified")
        
    elif select_1==3:
        select_2=int(input("Enter Roll_no modify:"))
        changes=int(input('Enter New Mark2:'))
        sql='Update home SET mark2=%s where roll_no=%s'
        mycursor.execute(sql,(changes,select_2))
        db.commit()
        print("Successfully modified")
        
    elif select_1==4:
        select_2=int(input("Enter Roll_no modify:"))
        changes=int(input('Enter New Mark1:'))
        sql='Update home SET mark3=%s where roll_no=%s'
        mycursor.execute(sql,(changes,select_2))
        db.commit()
        print("Successfully modified")
        
    elif select_1==5:
        select_2=int(input("Enter Roll_no modify:"))
        changes=int(input('Enter New Mark1:'))
        sql='Update home SET mark4=%s where roll_no=%s'
        mycursor.execute(sql,(changes,select_2))
        db.commit()
        print("Successfully modified")
        
    elif select_1==6:
        select_2=int(input("Enter Roll_no modify:"))
        changes=int(input('Enter New Mark1:'))
        sql='Update home SET mark5=%s where roll_no=%s'
        mycursor.execute(sql,(changes,select_2))
        db.commit()
        print("Successfully modified")