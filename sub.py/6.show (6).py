import pandas as pd
import mysql.connector

from matplotlib import pyplot as plt

db=mysql.connector.connect(
	host='localhost',
	user='root',
	password='pappy',
	database='visualizer'
	)

mycursor=db.cursor()

options=int(input('Select Operation:\n1.To Get Data about a student\n2.To view list of data\n3.To Insert data\n4.To update data\n5.To delete data\n6.Visualize student detail:'))

if options==6:
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
        
        

        a=['Mark1','Mark2','Mark3','Mark4','Nark5']
        b=list

        plt.bar(a,b)
        plt.xlabel('Subjects')
        plt.ylabel("Marks")
        plt.title(f'Marks of Roll_No:{roll}')
        plt.show()

        

    else:
        print('Invalid Request')










