import mysql.connector as sqltor
mycon=sqltor.connect(host="localhost",user="root",passwd="Monu@123",database="admin")

cursor=mycon.cursor()

c=1
cursor.execute("select max(n) from movie")
result = cursor.fetchone()
c = result[0] + 1 if result[0] else 1



print("WELCOME TO MOVIE TICKET BOOKING SYSTEM") 
print("-----------------------------------------------")
def login():
    ch=int(input('''ENTER YOUR LOGIN PROCESS
          1:USER LOGIN
          2:ADMIN LOGIN
            '''))
    if(ch==1):
        movie()
        
    else:
        ad=input("ENTER YOUR LOGIN NUMBER")
        adp=input("ENTER YOUR LOGIN PASSWORD")
        if(ad=="Monu@123") and (adp=="sachin"):
            print("WELCOME AT ADMIN PAGE")
            cursor.execute("select Name,moviename,theatre,timing,seat from movie")
            data=cursor.fetchall()
            for row in data:
                print("\n",row)
            login()   
        else:
            print("ENTER CORRECT PASSWORD OR LOGIN NUMBER!")
            login()
   
    
def movie():
    global c
    na=input("enter your name")
    print("WHICH MOVIE WANT TO WATCH:")
    print("----------------------------")
    print('''
     1: CIRCUS
     2: AVATAR(THE WAY OF WATER)
     3: FREDDY
        ''')
    mov=int(input())
    if(mov==1):
        s="insert into movie(n,Name,moviename)values({},'{}','{}')".format(c,na,'CIRCUS')
        cursor.execute(s)
        theatre()
    elif(mov==2):
        s="insert into movie(n,Name,moviename)values({},'{}','{}')".format(c,na,'AVATAR(THE WAY OF WATER')
        cursor.execute(s)
        theatre()
    elif(mov==3):
        s="insert into movie(n,Name,moviename)values({},'{}','{}')".format(c,na,'FREDDY')
        cursor.execute(s)
        theatre()

def theatre():
    global c
    print("MOVEI AVAILABLE IN THEATRES:")
    print("----------------------------")
    print('''
     1: INOX(Z SQUARE)
     2: PVR(SOUTH X)
     3: CARNIVAL CINEMAS(RAVE MOTI)
         ''')
    the=int(input())
    if(the==1):
        s="update movie set theatre='{}' where n={}".format('INOX(Z SQUARE)',c)
        cursor.execute(s)
        timing()
    elif(the==2):
        s="update movie set theatre='{}' where n={}".format('PVR(SOUTH X)',c)
        cursor.execute(s)
        timing()
    elif(the==3):
        s="update movie set theatre='{}' where n={}".format('CARNIVAL CINEMAS(RAVE MOTI)',c)
        cursor.execute(s)
        timing()

def timing():
    global c
    print("AVAILABLE SHOWS TIMING:")
    print("----------------------------")
    print('''
     1: 9:30-12:30
     2: 1:00-4:00
     3: 4:30-7:30
     4: 8:00-11:00
          ''')
    tim=int(input())
    if(tim==1):
        s="update movie set timing='{}' where n={}".format('9:30-12:30',c)
        cursor.execute(s)
        seat()
    elif(tim==2):
        s="update movie set timing='{}' where n={}".format('1:00-4:00',c)
        cursor.execute(s)
        seat()
    elif(tim==3):
        s="update movie set timing='{}' where n={}".format('4:30-7:30',c)
        cursor.execute(s)
        seat()
    elif(tim==4):
        s="update movie set timing='{}' where n={}".format('8:00-11:00',c)
        cursor.execute(s)
        seat()

def seat():
    global c
    print(''' SELECT YOUR SEATS:
          --------------------------

    1: GOLD - 190
    2: PLATINUM - 250
    3: RECLINER - 450
      ''')
    sea=int(input())

    if(sea==1):
        print("TOTAL AMOUNT PAYABLE:190")
        s="update movie set seat='{}' where n={}".format('GOLD',c)
        cursor.execute(s)
        mycon.commit()
        payment()
    elif(sea==2):
        print("TOTAL AMOUNT PAYABLE:250")
        s="update movie set seat='{}' where n={}".format('PLATINUM',c)
        cursor.execute(s)
        mycon.commit()
        payment()
    elif(sea==3):
        print("TOTAL AMOUNT PAYABLE:450")
        s="update movie set seat='{}' where n={}".format('RECLINER',c)
        cursor.execute(s)
        mycon.commit()
        payment()
        
    
def payment():
    global c
    inp=(c,)
    query="select Name,moviename,theatre,timing,seat from movie where n=%s"
    cursor.execute(query,inp)
    data=cursor.fetchall()
    print(data)
    
    print('''
             PAYMENT MODE
        -------------------------
            
     1: CREDIT/DEBIT CARD
     2: PHONEPAY/GPAY/PAYTM
     3: UPI ID
     ''')
    pay=int(input())
    if(pay==1):
        print("----------------------------")
        print("CREDIT CARD NUMBER - ")
        print("CREDIT CARD HOLDER NAME - ")
        print("CREDIT CARD CV NUMBER - ")
        print("ENTER THE OTP - ")
        print("PAYMENT DONE!")
        print("ENJOY YOUR MOVIE")
        c=c+1
        login()

        
    elif(pay==2):
        print("----------------------------")
        print("SCAN THE QR CODE")
        print("PAYMENT DONE!")
        print("ENJOY YOUR MOVIE")
        c=c+1
        login()

     
    elif(pay==3):
        print("----------------------------")
        print("ENTER YOUR VALID UPI ID")
        print("PAYMENT LINK SEND TO YOUR UPI ID")
        print("PAYMENT DONE!")
        print("ENJOY YOUR MOVIE")
        c=c+1
        login()
        
    else:
        print("Invalid payment option. Please try again.")
        payment()


login()
