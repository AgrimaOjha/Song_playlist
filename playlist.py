#importing mysql
import mysql.connector



#user name and password
user_id = ['agrima','snigdha']               
pwd = ['music']


                                        
user = input('\nEnter user ID: ')               
pd = input('Enter password: ')


if user in user_id and pd in pwd:
    print('\nWelcome,to your own music library',user+'!')
    print('\nEnjoy and love music')
    print('\nWhere Words fail, Music speaks')
    print('\U0001F917'*28)
    
    
    
else:
    print('\nOh no! Please try again. ')
    quit()
print('='*50)
#SQL connectivity
con=mysql.connector.connect(host='localhost',user='root',password='root',
                            database='sportify')


cur=con.cursor()
cur.execute('use sportify')
#insertion
def insertion():
    while True:
        n=int(input('Enter Song no.:= '))
        s=input("Enter Song name:= ")
        a=input("Enter Artist name:= ")
        g=input("Enter Genre of the song:= ")
        l=input("Enter Language of the song:= ")
        query="insert into favorites values(%s,'%s','%s','%s','%s')"%(n,s,a,g,l)
        cur.execute(query)
        con.commit()
        print("Records inserted successfully")
        ch=input("Do you want to enter more records?(y/n)")
        if ch=="n":
            break
    con.close()
    print('='*50)

#display
def display():
    cur.execute('select * from favorites')
    data=cur.fetchall()
    for i in data:
        print(i)
        
#deletion
def deletion():
    m=int(input("Enter Song no.= "))
    
    query='select * from favorites where sno={}'.format(m)
    cur.execute(query)
    data=cur.fetchall()
    for i in data:
        print(i)
    q1='delete from favorites where sno={}'.format(m)
    cur.execute(q1)
    con.commit()
    print ('Record deleted')
    print('='*50)


#update
def update():
    while True:
        n=int(input("Enter Song no.:= "))
    
        u=input('What do you want to update? \n\
                1. Song name\n\
                2. Artist name \n\
                3. Genre \n\
                4. Language\n\
                =:')
    
        if u=='1':
            o=input('Enter song name = ')
            cur.execute('update favorites set song_name="%s" where sno=%s'%(o,n))
            print ('update successful')
            con.commit()
            
        elif u=='2':
            a=input("Enter artist's name:= ")
            cur.execute('update favorites set artist_name="%s" where sno=%s'%(a,n))
            print ('update successful')
            con.commit()
            
        elif u=='3':
            d=input("Enter genre:= ")
            cur.execute('update favorites set genre="%s" where sno=%s'%(d,n))
            print ('update successful')
            con.commit()
            
        elif u=='4':
            l=input("Enter language:= ")
            cur.execute('update favorites set langugage="%s" where sno=%s'%(l,n))
            print ('update successful')
            con.commit()
        else:
            print('Enter valid option')
        r=input('Do you want to continue updating? (y/n)')
        if r=='n':
            break
    print('='*50)


#search
def search():
    while True:
        
        r=int(input('Enter sno:= '))
        query='select * from favorites where sno=%s'%(r,)
        cur.execute(query)
        data=cur.fetchall()
        for i in data :
            print(i)
        n=input('Do you want to continue searching? (y/n)')
        if n=='n':
            break
    print('='*50)

#main code
while True:
    o=input(' Enter 1 to Insert data \n Enter 2 to Display data\n Enter 3 to \
Update any data\n Enter 4 to Search any data \n Enter 5 to Delete any data \n Enter \
6 to Exit\n := ')
    if o=='1':
        insertion()
    elif o=='2':
        display()
    elif o=='3':
        update()
    elif o=='4':
        search()
    elif o=='5':
        deletion()
    elif o=='6':
        quit()
    else:
        print('Enter a valid option!!')
        break
              
print ('Hope you have listed all your favorite songs.\nPlease do come again!!!')
print ('\U0001F600'*28)
print ('='*50)    


        
        



    
    
    
