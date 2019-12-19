#
#
# For testing SQL Server connection in CSIL through pyodbc connection (using SQL Server standard login)
#
# You should run this program on a CSIL system. (verified with Python 3.6.2 64bit)
#
# Please modify this program before using.
#
# alternation includes: 
#
#       the standard SQL Server login (which is formatted as s_<username>)
#       the password for CSIL SQL Server standard login
#

import pyodbc

conn = pyodbc.connect('driver={SQL Server};server=cypress.csil.sfu.ca;uid=s_name;pwd=********')
# the name and the passport should be based on your own information 
#  ^^^ 2 values must be change for your own program.

#  Since the CSIL SQL Server has configured a default database for each user, there is no need to specify it (<username>354)
cur = conn.cursor()
print('\nThere are three operations in the program\n')
print('1.Search Listing and Book Listing  2.Write review\n')
operation = int(input('Please input your choice(type1,or 2)  : '))
print("operation =",operation)
while(operation<3):
    if operation==1:
        print('Please give the price range, number of bedrooms, and the dates in your search:')
        max_price = input("Maximum Price:")
        min_price = input("Minimum Price:")
        number_of_bedroom = input("Please input the number of bedrooms you want: ")
        new = "\'"
        start_date = input("Please input the start date you want(2000-00-00) : ")
        end_date =   input("Please input the end date you want  (2000-00-00) : ")
        start_date = new+start_date+new
        end_date=new+end_date+new

        SQLCommand=("SELECT DISTINCT L.id,L.name,LEFT(L.description,25),L.number_of_bedrooms,C.price "
                    "FROM Listings L,(SELECT * FROM Calendar WHERE date BETWEEN "+start_date+" AND "+end_date+")C "
                    "WHERE C.listing_id=L.id AND C.available=1 AND C.price>=10 AND C.price<=100 AND L.number_of_bedrooms="+number_of_bedroom)
        cur.execute(SQLCommand)
        results = cur.fetchone()
        if results==None:
            print('\nWhat You Search Is Not Exists!!!\n')  
            continue
        print('______________________________________________________________\n') 
        while results:             
            print ("Id:   " +  str(results[0]))  
            print ("Name: " +  str(results[1]))  
            print ("desp: " +  str(results[2]))  
            print ("#brs: " +  str(results[3]))  
            print ("Pri : " +  str(results[4]))  
            print()  
            results = cur.fetchone()       
    if operation==1:
        print('\nPlease Decide Your Booking: \nyou can enter the listing id and the date, your name and number of guests\n ')
        listing_IDs = input('Listing id: ')
        Name = input('Your Name : ')
        Guests =      input('#guests    :')
        new = "\'"
        #start_date =  input("start date: ")
       # end_date =    input("end date  : ")
        Name = new+Name+new
        #start_date = new+start_date+new
        #end_date=new+end_date+new
        SQLPre=("SELECT COUNT(*) FROM Bookings")
        cur.execute(SQLPre)
        results = cur.fetchone()
        ID_NUM=str(results[0]+2)
        SQLCommand=("INSERT INTO Bookings(id,listing_id,guest_name,stay_from,stay_to,number_of_guests) "
                    "VALUES ("+ID_NUM+","+ listing_IDs+","+Name+","+start_date+","+end_date+","+Guests+")")
        print(SQLCommand)
        cur.execute(SQLCommand)
        conn.commit()
        print("\n__________________________________________\nYour Next Step: 1. Searh and book again 2.Review Your Bookings 3.Quit \n")
        operation = int(input("Your Choice: "))
    if operation==2:
        Name=input("Please Input Your Name:  ")
        new = "\'"
        Name=new+Name+new
        SQLCommand=("SELECT * FROM Bookings WHERE guest_name="+Name)
        print(SQLCommand)
        cur.execute(SQLCommand)
        results = cur.fetchone()
        if results==None:
            print('\nYou have no bookings before!!!\n')  
            continue
        print('______________________________________________________________\n') 
        while results:             
            print ("Booking Id: " +  str(results[0]))  
            print ("Listing Id: " +  str(results[1]))  
            print ("Start Date: " +  str(results[3]))  
            print ("End Date  : " +  str(results[4]))  
            print ("Guests num: " +  str(results[5]))  
            print()  
            results = cur.fetchone()
        Review_id = input("Input the listing ID you want to review: ")
        Reviews   = input("Please Input Your Reviews: \n")
        Reviews=new+Reviews+new
        SQLPre = ("SELECT MAX(id) FROM Reviews")
        cur.execute(SQLPre)
        results = cur.fetchone()
        ID_NUM=str(results[0]+1)
        SQLCommand=("INSERT INTO Reviews (id,listing_id,comments,guest_name) VALUES ("+ID_NUM+","+Review_id+","+Reviews+","+Name+")")
        print(SQLCommand)
        try:
            cur.execute(SQLCommand)
        except Exception as error:
            print("Can not insert your review\nERROR: ")
            print(error)
        conn.commit()
    print("\n__________________________________________\nYour Next Step: 1. Searh and book again 2.Review Your Bookings 3.Quit \n")
    operation = int(input("Your Choice: "))
    
conn.close()

#  This program will output your CSIL SQL Server standard login,
#  If you see the output as s_<yourusername>, it means the connection is a success.
#  
#  You can now start working on your assignment.
# 
