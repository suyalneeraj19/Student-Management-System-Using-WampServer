import mysql.connector

            
def Update():
            conn=mysql.connector.connect(host='localhost',database='neeraj',user='root',password='')
            cursor=conn.cursor()
            print("\n \n \t \t \tFILL UP THE FOLLOWING DETAILS \n \n")
            s=input("ENTER STUDENTS SERIAL NUMBER:")
            name=input("ENTER STUDENT NAME:")
            fname=input("ENTER FATHER'S NAME:MR.")
            clas=input("ENTER STUDENT'S CLASS:")
            dob=input("ËNTER THE DATE OF BIRTH:")
            aad=input("ENTER AADHAR NUMBER:")
            mob=input("ENTER MOBILE NUMBER:")
            add=input("ENTER THE ADDRESS:")
            b=input("BORDER OR DAYSCHOLAR:")
            att=input("TOTAL NUMBER OF DAYS STUDENT ATTENDED THE SCHOOL:")
            
            sql="update abc set NAME='"+name+"',FATHERS_NAME='"+fname+"',STANDARD='"+clas+"' ,D_O_B='"+dob+"',AADHAR_NUMBER='"+aad+"',MOBILE_NUMBER='"+mob+"',ADDRESS='"+add+"',BORDER_OR_DAYSCHOLAR='"+b+"',ATTENDENCE='"+att+"' where SERIAL_NUMBER='"+s+"';"
            cursor.execute(sql)
            conn.commit()
            conn.close()
            print("\n \t \t \t \t ************THE DATA IS UPDATED SUCCESFULLY**************** \n \n \n")

def Display():
            conn=mysql.connector.connect(host='localhost',database='neeraj',user='root',password='')
            cursor=conn.cursor()
            sql='select * from abc;'
            cursor.execute(sql)
            records=cursor.fetchall()
            for record in records:
               print(record)
            conn.commit()    
            conn.close()
           

def Search():
           
            conn=mysql.connector.connect(host='localhost',database='neeraj',user='root',password='')
            cursor=conn.cursor()
            a=input("ENTER THE SERIAL NUMBER YOU WANT TO SEARCH:")
            sql='select * from abc where SERIAL_NUMBER=%s'
            c=conn.cursor(buffered=True)
            data = (a,)
            c.execute(sql,data)
            r=c.rowcount
            found=False
            if(r==1):
                found=True
            else:
                found=False
            print(found)    
            if(found):
                print("\n")
                sql='select * from abc where SERIAL_NUMBER="'+a+'";'
                cursor.execute(sql)
                records=cursor.fetchall()
                for record in records:
                    print(record)
            else:
                print('\n')
                print("THERE IS NO SUCH REGISTERED SERIAL_NO_")
            
            print('\n \n \n \t \t \t \t   *****************THANKS FOR CHOOSING US*************** \n \n \n')
        
            
def Delete():
            conn=mysql.connector.connect(host='localhost',database='neeraj',user='root',password='')
            cursor=conn.cursor()
            print("\n \n \t \t ENTER THE NAME WHOSE DATA YOU WANT TO DELETE")
            a=input("NAME:")
            sql='delete from abc where name="'+a+'";'
            cursor.execute(sql)
            records=cursor.fetchall()
            for record in records:
                print(record)
            conn.commit()
            conn.close()
            conn=mysql.connector.connect(host='localhost',database='neeraj',user='root',password='')
            cursor=conn.cursor()
            sql='delete from result where name="'+a+'";'
            cursor.execute(sql)
            records=cursor.fetchall()
            for record in records:
                print(record)
            conn.commit()
            conn.close()
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\t THANK YOU \t ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",'\n')
            
def Lock():
        conn=mysql.connector.connect(host='localhost',database='neeraj',user='root',password='')
        cursor=conn.cursor()
        print("\t**************ONLY ADMINS CAN ACESS THIS FUNCTION************** \n")
        user=input("ENTER USERNAME:")
        password=input("ENTER PASSWORD:")
        if(user=="NEERAJ SUYAL" and password=="SUYAL123"):
            print('\n')
            Display()
        else:
            print("WRONG USER ID OR PASSWORD \n")    
        conn.commit()
        conn.close()
        
def Menu():
    f=True
    while(f):
        print('\n')
        print("1.TO INPUT MARKS \n")
        print("2.DISPLAY MARKS \n")
        print("3.TO DISPLAY TOPPER \n")
        print("4.TO DISPLAY ALL STUDENTS WHO HAVE PASSESD \n")
        print("5.TO DISPLAY ALL STUDENTS WHO HAVE FAILED \n")
        print("6.TO SEARCH FOR SPECIFIC STUDENT MARKS \n")
        print("7.TO EXIT")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",'\n')
        ch=int(input("ENTER YOUR CHOICE:"))
        if(ch==1):
            print('\n')
            def Marks():
                conn=mysql.connector.connect(host='localhost',database='neeraj',user='root',password='')
                cursor=conn.cursor()
                s=input("ENTER STUDENTS SERIAL NUMBER:")
                
                E=float(input("ENTER ENGLISH MARKS:")) 
                M=float(input("ENTER MATHS MARKS:")) 
                P=float(input("ENTER PHYSIC'S MARKS:")) 
                C=float(input("ENTER CHEMISTRY'S MARKS:"))
                CO=float(input("ENTER COMPUTER'S MARKS:"))
                x=E+M+P+C+CO
                d=(x/500)*100   
                print("TOTAL MARKS ARE:",x)
                print("THE PERCENTAGE IS:",d,"%")
                E=str(E)
                M=str(M)
                P=str(P)
                C=str(C)
                CO=str(CO)
                x=str(x)
                d=str(d)
                sql="update result  set ENGLISH='"+E+"',MATHS='"+M+"',PHYSICS='"+P+"',CHEMISTRY='"+C+"',COMPUTER='"+CO+"',TOTAL='"+x+"',PERCENTAGE='"+d+"' where SERIAL_NUMBER='"+s+"';"        
                cursor.execute(sql)
                conn.commit()
                conn.close()
                print("\n \t \t \t \t ************THE DATA IS UPDATED SUCCESFULLY****************\n")
            Marks()
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",'\n')
        elif(ch==2):
            print('\n')
            def Showdata():
                conn=mysql.connector.connect(host='localhost',database='neeraj',user='root',password='')
                cursor=conn.cursor()
                sql='select * from result;'
                cursor.execute(sql)
                records=cursor.fetchall()
                for record in records:
                    print(record)
                conn.commit()    
                conn.close()
            Showdata()
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",'\n')
        elif(ch==3):
            print('\n')
            def Topper():
                conn=mysql.connector.connect(host='localhost',database='neeraj',user='root',password='')
                cursor=conn.cursor()
                sql='select * from result order by PERCENTAGE desc LIMIT 1 ;'
                cursor.execute(sql)
                records=cursor.fetchall()
                for record in records:
                    print(record)
                conn.commit()    
                conn.close()
            Topper() 
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",'\n')
        elif(ch==4):
            print('\n')
            def Passed():
                conn=mysql.connector.connect(host='localhost',database='neeraj',user='root',password='')
                cursor=conn.cursor()
                sql='select * from result where PERCENTAGE>=50;'
                cursor.execute(sql)
                records=cursor.fetchall()
                for record in records:
                    print(record)
                conn.commit()    
                conn.close()                            
            Passed()
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",'\n')
        elif(ch==5):
            print('\n')
            def Failed():
                conn=mysql.connector.connect(host='localhost',database='neeraj',user='root',password='')
                cursor=conn.cursor()
                sql='select * from result where PERCENTAGE<50;'
                cursor.execute(sql)
                records=cursor.fetchall()
                for record in records:
                    print(record)
                conn.commit()    
                conn.close()                            
            Failed()
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",'\n')
        elif(ch==6):
            print('\n')
            def Student():
                conn=mysql.connector.connect(host='localhost',database='neeraj',user='root',password='')
                cursor=conn.cursor()
                a=input("ENTER THE SERIAL_NUMBER YOU WANT TO SEARCH:")
                sql='select * from result where SERIAL_NO_=%s'
                c=conn.cursor(buffered=True)
                data = (a,)
                c.execute(sql,data)
                r=c.rowcount
                found=False
                if(r==1):
                    found=True
                else:
                    found=False
                if(found):
                    print("\n")
                    sql='select * from result where SERIAL_NUMBER="'+a+'";'
                    cursor.execute(sql)
                    records=cursor.fetchall()
                    for record in records:
                        print(record)
                else:
                    print('\n')
                    print("THERE IS NO SUCH REGISTERED SERIAL_NUMBER")
            Student()
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",'\n')
        elif(ch==7):
            f=False
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\t THANK YOU \t ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",'\n')
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",'\n')
        else:
            print(" \n \n \t \t \t \t \t   ****************************INVALID INPUT****************************** \t \n \n \n")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",'\n')
                
def Count():
        conn=mysql.connector.connect(host='localhost',database='neeraj',user='root',password='')
        cursor=conn.cursor()
        sql='select count(SERIAL_NUMBER) from abc;'
        cursor.execute(sql)
        records=cursor.fetchall()
        for record in records:
            print(record)
        conn.commit()
        conn.close()                    
        
def Menu1():
    f=True
    while(f):
        print('\n')
        print("1.TO FIND STUDENT'S BASIC INFORMATION \n")
        print("2.TO FIND STUDENT'S AADHAR NUMBER \n")
        print("3.TO SEARCH HOW MANY DAYS A STUDENT IS PRESENT\n")        
        print("4.TO SEARCH WHAT PERCENTAGE HE/SHE HAS SCORED \n")
        print("5.TO SEARCH STUDENT'S DATE OF BIRTH \n")
        print("6.TO SEARCH HOW MANY STUDENT LIVE IN A SPECIFIC ADDRESS \n")
        print("7.TO EXIT")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",'\n')
        ch=int(input("ENTER YOUR CHOICE:"))
        if(ch==1):
            def basic():
                print('\n')
                conn=mysql.connector.connect(host='localhost',database='neeraj',user='root',password='')
                cursor=conn.cursor()
                a=input("ENTER STUDENT'S NAME:")
                sql='select * from abc where name="'+a+'";'
                cursor.execute(sql)
                records=cursor.fetchall()
                for record in records:
                                
                    print('\n',"SERIAL NUMBER:",record[0], '\n' ,"NAME:",record[1] ,'\n' ,"FATHER'S NAME:",record[2] ,'\n' ,"STANDARD:",record[3] , '\n' ,"MOBILE NUMBER:",record[6], '\n' )
                conn.commit()    
                conn.close()
            basic()    
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",'\n')
            
            
        elif(ch==2):
             def aadhar():   
                print('\n')
                conn=mysql.connector.connect(host='localhost',database='neeraj',user='root',password='')
                cursor=conn.cursor()
                a=input("ENTER STUDENT'S NAME:")
                sql='select * from abc where name="'+a+'";'
                cursor.execute(sql)
                records=cursor.fetchall()
                for record in records: 
                    print('\n',"SERIAL NUMBER:",record[0], '\n' ,"NAME:",record[1] ,'\n',"AADHAR NUMBER:",record[5],'\n')
                conn.commit()    
                conn.close()
             aadhar()       
             print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",'\n')


        elif(ch==3):
            print('\n')
            def attendence():
                conn=mysql.connector.connect(host='localhost',database='neeraj',user='root',password='')
                cursor=conn.cursor()
                a=input("ENTER A NAME:")
                sql='select * from abc where name="'+a+'";'
                cursor.execute(sql)
                records=cursor.fetchall()
                for record in records:
                    print('\n',"SERIAL NUMBER:",record[0], '\n' ,"NAME:",record[1] ,'\n',"ATTENDENCE:",record[9], "DAYS",'\n' )
                conn.commit()    
                conn.close()
            attendence() 
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",'\n')
        elif(ch==4):
            print('\n')
            def percentage():
                conn=mysql.connector.connect(host='localhost',database='neeraj',user='root',password='')
                cursor=conn.cursor()
                a=input("ENTER A NAME:")
                sql='select * from result where name="'+a+'";'
                cursor.execute(sql)
                records=cursor.fetchall()
                for record in records:
                    print('\n',"SERIAL NUMBER:",record[0], '\n' ,"NAME:",record[1] ,'\n',"PERCENTAGE SCORED:",record[8],"%",'\n')
                conn.commit()    
                conn.close()                            
            percentage()
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",'\n')
        elif(ch==5):
            print('\n')
            def date():
                conn=mysql.connector.connect(host='localhost',database='neeraj',user='root',password='')
                cursor=conn.cursor()
                a=input("ENTER STUDENT'S NAME:")
                sql='select * from abc where name="'+a+'";'
                cursor.execute(sql)
                records=cursor.fetchall()
                for record in records:
                    print('\n',"SERIAL NUMBER:",record[0], '\n' ,"NAME:",record[1] ,'\n',"DATE OF BIRTH:",record[4],'\n')
                conn.commit()    
                conn.close()                            
            date()
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",'\n')
        elif(ch==6):
            print('\n')
            def address():
                conn=mysql.connector.connect(host='localhost',database='neeraj',user='root',password='')
                cursor=conn.cursor()
                a=input("ENTER THE ADDRESS YOU WANT TO LOCATE:")
                sql='select * from abc where  ADDRESS=%s;'
                c=conn.cursor(buffered=True)
                data = (a,)
                c.execute(sql,data)
                r=c.rowcount
                found=False
                if(r==1):
                    found=True
                else:
                    found=False
                
                if(found):
                    print("\n")
                    
                    sql='select * from abc where ADDRESS="'+a+'";'                    
                    cursor.execute(sql)
                    records=cursor.fetchall()
                    for record in records:
                        print('\n',"SERIAL NUMBER:",record[0], '\n' ,"NAME:",record[1])
                    conn.commit()    
                    conn.close()
                else:
                     print('\n')
                     print("THERE IS NO SUCH REGISTERED ADDRESS")
                     conn.commit()    
                     conn.close()   
            address()
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",'\n')
        elif(ch==7):
            f=False
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\t THANK YOU \t ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",'\n')
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",'\n')
        else:
            print(" \n \n \t \t \t \t \t   ****************************INVALID INPUT****************************** \t \n \n \n")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",'\n')


def REGISTRATION():
            conn=mysql.connector.connect(host='localhost',database='neeraj',user='root',password='')
            cursor=conn.cursor()
            print("\n \n \t \t \tFILL UP THE FOLLOWING DETAILS \n \n")
            a=input("ENTER THE AADHAR NUMBER:")
            sql='select * from abc where AADHAR_NUMBER=%s'
            c=conn.cursor(buffered=True)
            data = (a,)
            c.execute(sql,data)
            r=c.rowcount
            found=False
            if(r==1):
                found=True                             
            else:
                found=False
            if(found):
               
                name=input("ENTER STUDENT NAME:")
                fname=input("ENTER FATHER'S NAME:MR.")
                clas=input("ENTER STUDENT'S CLASS:")
                dob=input("ËNTER THE DATE OF BIRTH:")
                aad=a
                mob=input("ENTER MOBILE NUMBER:")
                add=input("ENTER THE ADDRESS:")
                b=input("BORDER OR DAYSCHOLAR:")
                att=input("TOTAL NUMBER OF DAYS STUDENT ATTENDED THE SCHOOL:")    
                sql='insert into abc(name,fathers_name,STANDARD,D_O_B,AADHAR_NUMBER,MOBILE_NUMBER,ADDRESS,BORDER_OR_DAYSCHOLAR,ATTENDENCE)values ("'+name+'","'+fname+'","'+clas+'","'+dob+'","'+aad+'","'+mob+'","'+add+'","'+b+'","'+att+'")';
                cursor.execute(sql)
                conn.commit()
                conn.close()
                conn=mysql.connector.connect(host='localhost',database='neeraj',user='root',password='')
                cursor=conn.cursor()
                sql='insert into result(name)values("'+name+'")';
                cursor.execute(sql)
                conn.commit()
                conn.close()
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",'\n')
               
            else:
                print('\n')
                print("INVALID AADHAR NUMBER")
                cursor.execute(sql)
                conn.commit()
                conn.close()
                print('\n')
                print('\n')
                
                a=input("ENTER THE AADHAR NUMBER:")
                name=input("ENTER STUDENT NAME:")
                fname=input("ENTER FATHER'S NAME:MR.")
                clas=input("ENTER STUDENT'S CLASS:")
                dob=input("ËNTER THE DATE OF BIRTH:")
                aad=a
                mob=input("ENTER MOBILE NUMBER:")
                add=input("ENTER THE ADDRESS:")
                b=input("BORDER OR DAYSCHOLAR:")
                att=input("TOTAL NUMBER OF DAYS STUDENT ATTENDED THE SCHOOL:")    
                sql='insert into abc(name,fathers_name,STANDARD,D_O_B,AADHAR_NUMBER,MOBILE_NUMBER,ADDRESS,BORDER_OR_DAYSCHOLAR,ATTENDENCE)values ("'+name+'","'+fname+'","'+clas+'","'+dob+'","'+aad+'","'+mob+'","'+add+'","'+b+'","'+att+'")';
                cursor.execute(sql)
                conn.commit()
                conn.close()
                conn=mysql.connector.connect(host='localhost',database='neeraj',user='root',password='')
                cursor=conn.cursor()
                sql='insert into result(name)values("'+name+'")';
                cursor.execute(sql)
                conn.commit()
                conn.close()
        
          
user=input("ENTER YOUR USER ID:")
password=input("ENTER YOUR PASSWORD:")
f=False
if(user=="NEERAJ SUYAL" and password=="SUYAL123"):
    f=True
    print('\n \n \n')
elif(user=="1" and password=="1"):
    f=True 
    print('\n \n \n')
elif(user=="ARYAN SELWAL" and password=="SELWAL123"):
    f=True 
    print('\n \n \n')    
elif(user=="HUMAM AHMED" and password=="AHMED123"):
    f=True
    print('\n \n \n')
elif(user=="ABHISHEK RATHORE" and password=="RATHORE123"):
    f=True
    print('\n \n \n')
else:
     print("\t \t \t \t*************YOU ARE NOT A REGISTERED USER************  \n \n")     
while(f):
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",'\n')
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~STUDENT MANAGMENT SYSTEM~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",'\n')
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",'\n')
    print("1.REGISTRATION \n")
    print("2.UPDATE \n")
    print("3.DISPLAY \n")
    print("4.SEARCH \n")
    print("5.DELETE \n")
    print("6.STUDENT'S INFORMATION \n")
    print("7.REPORT CARD \n ")
    print("8.TOTAL NUMBER OF STUDENT REGISTERED \n ")
    print("9.EXIT \n")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",'\n')
    ch=int(input("ENTER YOUR CHOICE:"))
    if(ch==1):
        print('\n')
        REGISTRATION()
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",'\n')
       
    elif(ch==2):
        print('\n')
        Update()
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",'\n')
        
    elif(ch==3):
        print('\n')
        Lock()
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",'\n')    
    elif(ch==4):
        print('\n')
        Search()
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",'\n')
    elif(ch==5):
        print('\n')
        Delete()
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",'\n')
    elif(ch==6):
        print('\n')
        Menu1()
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",'\n')
    elif(ch==7):
        print('\n')
        Menu()
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",'\n')
    elif(ch==8):
        print('\n')
        Count()
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",'\n')
    elif(ch==9):
        print('\n')
        f=False
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\t THANK YOU \t ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",'\n')
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",'\n')
    else:
        print(" \n \n \t  \t \t \t ****************************INVALID INPUT****************************** \t \n \n \n")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",'\n')





''''create table result(SERIAL_NUMBER  MEDIUMINT NOT NULL AUTO_INCREMENT,NAME varchar(20),ENGLISH varchar(20),MATHS varchar(20),PHYSICS varchar(20),CHEMISTRY varchar(20),COMPUTER  varchar(20),TOTAL int(20),PERCENTAGE int(30),PRIMARY KEY(SERIAL_NUMBER));

create table abc(SERIAL_NUMBER MEDIUMINT NOT NULL AUTO_INCREMENT,NAME  varchar(30),FATHERS_NAME varchar(30),STANDARD varchar(30),D_O_B varchar(30),AADHAR_NUMBER varchar(30),MOBILE_NUMBER varchar(10),ADDRESS varchar(30),BORDER_OR_DAYSCHOLAR varchar(30),ATTENDENCE  varchar(12),PRIMARY KEY(SERIAL_NUMBER));'''

''''con = mysql.connector.connect(host='localhost', database='banking', user='root', password='')
    cursor = con.cursor()
    acc=input("Enter Account Number")
    sql = 'select * from bank where acc=%s'
    c = con.cursor(buffered=True)
    data = (acc,)
    c.execute(sql, data)
 
    r = c.rowcount
    found=False
    if r == 1:
        found= True
    else:
        found= False
    if(found):
        print("Dear Customer Your Current Account Balance is: ",end='')
        sql ='select ammount from bank where acc="'+acc+'";'
        cursor.execute(sql)
        records = cursor.fetchall()
        for record in records:
            print(record)
    else:
        print("There is No account number: ",acc)'''
        
'''conn=mysql.connector.connect(host='localhost',database='neeraj',user='root',password='')
            cursor=conn.cursor()
            sql='select * from abc;'
            cursor.execute(sql)
            records=cursor.fetchall()
            for record in records:
                print('\n')                
                print("SERIAL NUMBER:",record[0],"NAME:",record[1],"FATHER'S NAME:",record[2],"STANDARD:",record[3],"DATE OF BIRTH:",record[4],"MOBILE NUMBER:",record[5],"ADDRESS:",record[6],"BORDER/DAYSCHOLA:",record[7],"ATTENDENCE:",record[8])
            conn.commit()    
            conn.close()'''       