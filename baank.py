import random
import mysql.connector
sqlcon=mysql.connector.connect(host='localhost', user='root', password='faraazzuberi', database='faraaz')
cursor=sqlcon.cursor()



def welcome(): 
    print("Welcome to our online banking platform") 
    print('-'*50) 
    print("Please choose an option")
    print('-'*23)
    L=int(input("1. Create a new account \n2. Login (if you already have an existing account \nEnter your choice (1 or 2): "))
    print('-'*50)
    
    if L==1:
        def userr():
            global user
            global fname
            global sname
            fname=input("Please enter your first name: ")
            sname=input("Please enter your surname: ")
            user=input("Please give a username for your account: ")

        def password(): 
            global password_inp
            password_inp=input("Please enter a password (must contain letters and numbers): ")
            password_check=input("Please confirm your password: ")
            if password_inp==password_check: 
                print("Thank you for creating an account with us. \nWelcome!")
            else:
                print("Passwords do not match")
                password()
        userr()
        password()
        newuser_query=("INSERT INTO bank(Customer_UserID, Bank_Acc_Num, Customer_Fname, Customer_Surname, Account_balance, Customer_since, password) VALUES('{}', {}, '{}', '{}', {}, '{}', '{}')".format(user, random.randint(100,1000), fname, sname, 2500,'2022-2-11' , password_inp))
        cursor.execute(newuser_query)
        sqlcon.commit()
    elif L==2: 
        def passs():
            global user
            user=input("Enter your username: ")
            select_q="SELECT * FROM bank WHERE Customer_UserID='{}'".format(user)
            cursor.execute(select_q)
            abc=cursor.fetchall()
            row_count=cursor.rowcount
            if row_count>0:
                global pas
                global sp
                q2="SELECT password FROM bank WHERE Customer_UserID='{}'".format(user)
                cursor.execute(q2)
                sp=cursor.fetchone()
                pas=input("Please enter your password: ")
                print(sp)
                pascheck=(sp[0])      
                if pas==pascheck:
                    fname="SELECT Customer_Fname FROM bank WHERE Customer_UserID='{}'".format(user)
                    cursor.execute(fname)
                    fet=cursor.fetchone()
                    fet0=(fet[0])
                    lname="SELECT Customer_Surname FROM bank WHERE Customer_UserID='{}'".format(user)
                    cursor.execute(lname)
                    fet2=cursor.fetchone()
                    fet2_0=(fet2[0])
                    print("Welcome", fet0, fet2_0) 
                else:
                    print("Incorrect password. Please try again.")
                    passs()
            else:
                print("User does not exist")
                opt=int(input("1. Try again? \nor \n2. Create account \n:-"))
                if opt==1: 
                    passs()
                elif opt==2:
                    print("You are being redirected to the homepage")
                    print('* '*20)
                    welcome()

        passs()
welcome()
def UI(): 
    print("What would you like to do today?")
    option=int(input("1. Add funds \n2. Transfer money \n3. Check account balance \n:-"))
    if option==1:
        fund=int(input("How much would you like to add? \n:-"))
        print("You have sucessfully added the funds to your account.")
        fd="UPDATE bank SET Account_balance=Account_balance+{} where Customer_UserID='{}'".format(fund, user)
        cursor.execute(fd)
        sqlcon.commit()
        balance_ch="SELECT Account_Balance FROM bank WHERE Customer_UserID='{}'".format(user)
        cursor.execute(balance_ch)
        curs=cursor.fetchone()
        curss=(curs[0])
        print("Your new account balance is ", curss)

    elif option==2:
        global choice
        choice=input("Enter the username of the account you would like to transfer to: ")
        ch="SELECT * FROM bank WHERE Customer_UserID='{}'".format(choice)
        cursor.execute(ch)
        lol=cursor.fetchall()
        rowss=cursor.rowcount
        if rowss>0:
            this=int(input("How much would you like to transfer? "))
            kk="UPDATE bank SET Account_balance=Account_balance-{} WHERE Customer_UserID='{}'".format(this, user)
            cursor.execute(kk)
            sqlcon.commit()
            trafs="UPDATE bank SET Account_balance=Account_balance+{} WHERE Customer_UserID='{}'".format(this, choice)
            cursor.execute(trafs)
            sqlcon.commit()
            lk="SELECT Account_Balance FROM bank WHERE Customer_UserID='{}'".format(user)
            cursor.execute(lk)
            xd=cursor.fetchone()
            dx=(xd[0])
            print("Your new account balance is ", dx)
    elif option==3: 
        blc="SELECT Account_balance FROM bank WHERE Customer_UserID='{}'".format(user)
        cursor.execute(blc)
        ftch=cursor.fetchone()
        fch=(ftch[0])
        print("Your account balance is ", fch)
    P=int(input("Is there something else you would like to do? \n1. Yes \nor \n2. No \n:-"))
    if P==1:
        UI()
    else:
        quit()
UI()
