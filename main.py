import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt

db=mysql.connector.connect(       # creating a connection for database
	host='localhost',
	user='root',
	password='pappy',
	database='visualizer'
	)

mycursor=db.cursor()            # creating a cursor

options=int(input('Select Operation:\n1.To Get Data about a student\n2.To view list of data\n3.To Insert data\n4.To update data\n5.To delete data\n6.Display in chart:\t')) # Receives action from user 

if options==1:                                                            #1.To view about a  particular student in database 
    no=int(input('Enter Roll_No to view the data:'))

    mycursor.execute('Select * from home where roll_no=%s',(no,))  
    result=mycursor.fetchone()

    if result is not None:
        print("One Data Found")
        for m in result:
            print(m)
    else:
       print("Something went wrong")

elif options==2:                                                          #2 To select all in database table
    sql='SELECT * from home'
    mycursor.execute(sql)
    for a in mycursor:
        print(a)

elif options==3:                                                          #3 To insert new data from the user
    
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

elif options==4:                                                       #4 To update details in Database 
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


elif options==5:                                                                #5 To Delete data in database
    choice=int(input('Enter Roll_No to delete the data'))

    mycursor.execute('DELETE FROM home WHERE roll_no=%s',(choice,))

    db.commit()
    print('Record was deleted successfully')

elif options==6:                                                                 #6 To display data in chart
    roll=int(input("Enter Roll_no of student"))

    
    mycursor.execute('Select mark1,mark2,mark3,mark4,mark5 from home where roll_no=%s',(roll,))
    result=mycursor.fetchone()

    if result is not None:
        print('One data found')

        df=pd.DataFrame(columns=['mark1','mark2','mark3','mark4','mark5']) # creating an empty dataframe
        list=list(result) # result from sql is stored in a list
     

        df.loc[len(df)]=list # appending the list to dataframe
        print(df)
        
       # y=np.array(list)
        
        

        a=['Mark1','Mark2','Mark3','Mark4','Mark5']
        b=list

        plt.bar(a,b)
        plt.xlabel('Subjects')
        plt.ylabel("Marks")
        plt.title(f'Marks of Roll_No:{roll}')
        plt.show()

        

    else:
        print('Invalid Request')
