import mysql.connector
import pandas as pd

db=mysql.connector.connect(
	host='localhost',
	user='root',
	password='pappy',
	database='visualizer'
	)

mycursor=db.cursor()


options=int(input('Select Operation:\n1.To Get Data about a student\n2.To view list of data\n3.To Insert data\n4.To update data\n5.To delete data'))

if options==3:
    
    def expo():
        export=int(input("Select format for export:\n\t1.CSV\n\t2.Excel\n\t3.Text\n\t4.View Dataframe "))
        if export==1:
            df.to_csv('std.csv')
        elif export==2:
            df.to_excel('std.xlsx')
        elif export==3:
            df.to_csv('std.txt',sep=" ")
        elif export==4:
            print(df)



    df=pd.DataFrame(columns=['Name','Roll_No','Mark1','Mark2','Mark3','Mark4','Mark5'])


    record=int(input("Enter how many records ar you want to insert:\t"))

    for h in range(record):
        name=input("Enter Name")
        roll_no=int(input('Enter your Roll_No'))
        mark1=int(input("Enter mark1"))
        mark2=int(input("Enter mark2"))
        mark3=int(input("Enter mark3"))
        mark4=int(input("Enter mark4"))
        mark5=int(input("Enter mark5"))
        print("One Record inserted")

        df.loc[h]=[name,roll_no,mark1,mark2,mark3,mark4,mark5]

        sql='Insert  into home(name,mark1,mark2,mark3,mark4,mark5,roll_no)values(%s,%s,%s,%s,%s,%s,%s)'
        data=(name,mark1,mark2,mark3,mark4,mark5,roll_no)

        mycursor.execute(sql,data)
        db.commit()

        expo()