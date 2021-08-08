import sqlite3 



def check_user(email,password):
    connection = sqlite3.connect('flask_sandy.db' , check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM  administrator WHERE email = ? and password = ?;",(email,password))
    ##print("Fetching single row")
    record = cursor.fetchone()
    
    if record:
     ##print(record[1]) print fullname
    
     message=True
    
    else:
    
     message = False
    
    return message
    
 
def get_user_id(email):
    connection = sqlite3.connect('flask_sandy.db' , check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM  administrator WHERE email = ?;",[email])
    record = cursor.fetchone()
    
    return record[0] 
    

 
def get_user_name(id):
    connection = sqlite3.connect('flask_sandy.db' , check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM  administrator WHERE admin_id = ?;",[id])
    record = cursor.fetchone()
    
    return record[1] 
        
    
def get_user_role(email):
    connection = sqlite3.connect('flask_sandy.db' , check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM  administrator WHERE email = ?;",[email])
    record = cursor.fetchone()
    
    return record[4]        
    
def check_email_exist(email):
    connection = sqlite3.connect('flask_sandy.db' , check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM  administrator WHERE email = ?;",[email])
    ##print("Fetching single row")
    record = cursor.fetchone()
    
    if record:
     ##print(record[1]) print fullname
     message=True;
    
    else:
    
     message = False;
    
    return message;    
    
    
    
def new_user(fname,email,password):

  try:
    connection = sqlite3.connect('flask_sandy.db' , check_same_thread = False)
    cursor = connection.cursor()
    sqlite_insert_query = """
    INSERT INTO administrator(
    fullname,
    email,
    password
    ) VALUES(?,?,?);"""
    
    
    if check_email_exist(email):
       print("Email already taken. Please use a different email address.")
    
    else:
    
    
# This is the qmark style:
       
       new_user= cursor.execute(sqlite_insert_query,[fname,email,password])
    connection.commit()
    print("New user successfully added : ", cursor.rowcount)
    cursor.close()
   
  except sqlite3.Error as error:
    print("Failed to add new user : ", error)
  finally:
    if connection:
       connection.close()
        
    
