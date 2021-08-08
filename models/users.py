import sqlite3


def check_user(email,password):
    connection = sqlite3.connect('flask_sandy.db' , check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM  users WHERE email = ? and password = ?;",(email,password))
    ##print("Fetching single row")
    record = cursor.fetchone()
    
    if record:
     ##print(record[1]) print fullname
     message=True;
    
    else:
    
     message = False;
    
    return message;
    
    
def user_details_diplayID(id):

    connection = sqlite3.connect('flask_sandy.db' , check_same_thread = False)
    cursor = connection.cursor()

## defining the Query
    query = "SELECT * FROM users WHERE user_id=?"

## getting records from the table
    cursor.execute(query, [id])

## fetching all records from the 'cursor' object
    records = cursor.fetchone()
    
    if records == "None":
    
      tasks = ""
    
    else:
      tasks = records  
      
      return  tasks


    
def reassignTask(user_id,task_id):
    """
    Update reassign task table
    :param conn: Connection to the SQLite database
    :return:
    """
    connection = sqlite3.connect('flask_sandy.db' , check_same_thread = False)
    cursor = connection.cursor()
    ###delete user first
    try:
       
        cursor.execute("update tasks set user_id=?  where task_id=?", [user_id,task_id])
    
        connection.commit()
        print("Task successlly reassigned ")
        cursor.close()
   
    except sqlite3.Error as error:
        print("Failed to reassign task, error: ", error)
    finally:
     if connection:
        connection.close()
        
    
    return True;    
    
    
    
def get_userid(email):
    connection = sqlite3.connect('flask_sandy.db' , check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM  users WHERE email = ?;",[email])
    ##print("Fetching single row")
    record = cursor.fetchone()
  
    
    return record[0];   
    
    
def TotalSignUps():
    connection = sqlite3.connect('flask_sandy.db' , check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM  users;")
    ##print("Fetching all row")
    record = len(cursor.fetchall())
    
     
    return record;
    
    
def SignUpsDisplayLimit5():
    connection = sqlite3.connect('flask_sandy.db' , check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM  users ORDER BY user_id DESC LIMIT 5;")
    ##print("Fetching all row")
    record = cursor.fetchall()
    
     
    return record; 
    
    
def SignUpsDisplay():
    connection = sqlite3.connect('flask_sandy.db' , check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM  users;")
    ##print("Fetching all row")
    record = cursor.fetchall()
    
     
    return record;
    
    
def UserReassignList(exclude_id):
    connection = sqlite3.connect('flask_sandy.db' , check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM  users WHERE user_id != ?;",[exclude_id])
    ##print("Fetching all row")
    record = cursor.fetchall()
    
     
    return record;    
             
        
    
def TotalSignUps_last_24hr():

    connection = sqlite3.connect('flask_sandy.db' , check_same_thread = False)
    cursor = connection.cursor()

## defining the Query
    query = 'SELECT * FROM users WHERE timestamp  > datetime(\'now\', \'-24 hour\') ORDER BY user_id DESC LIMIT 5;' 


    ##query = "SELECT * FROM tasks"

## getting records from the table
    cursor.execute(query)

## fetching all records from the 'cursor' object
    records = len(cursor.fetchall())
    
    if records == "None":
    
      tasks = ""
    
    else:
      tasks = records  
      
      return  tasks
      
      
       
def TotalSignUps_last_24hr_display():

    connection = sqlite3.connect('flask_sandy.db' , check_same_thread = False)
    cursor = connection.cursor()

## defining the Query
    query = 'SELECT * FROM users WHERE timestamp  > datetime(\'now\', \'-24 hour\') ORDER BY user_id DESC LIMIT 5;' 


    ##query = "SELECT * FROM tasks"

## getting records from the table
    cursor.execute(query)

## fetching all records from the 'cursor' object
    records = cursor.fetchall()
    
    if records == "None":
    
      tasks = ""
    
    else:
      tasks = records  
      
      return  tasks 


 
    


def TotalSignUps_last_Week():

    connection = sqlite3.connect('flask_sandy.db' , check_same_thread = False)
    cursor = connection.cursor()

## defining the Query
    query = 'SELECT * FROM users WHERE timestamp  BETWEEN datetime(\'now\', \'-6 days\') AND datetime(\'now\', \'localtime\') ORDER BY 	user_id DESC LIMIT 5;' 


    ##query = "SELECT * FROM tasks"

## getting records from the table
    cursor.execute(query)

## fetching all records from the 'cursor' object
    records = cursor.fetchall()
    
    if records == "None":
    
      tasks = ""
    
    else:
      tasks = records  
      
      return  tasks 
  
 
 
 
def TodaySignUps():

    connection = sqlite3.connect('flask_sandy.db' , check_same_thread = False)
    cursor = connection.cursor()

## defining the Query
    query = 'SELECT * FROM users WHERE timestamp  >= datetime(\'now\', \'start of day\') ORDER BY user_id DESC LIMIT 5;' 


    ##query = "SELECT * FROM tasks"

## getting records from the table
    cursor.execute(query)

## fetching all records from the 'cursor' object
    records = cursor.fetchall()
    
    if records == "None":
    
      tasks = ""
    
    else:
      tasks = records  
      
      return  tasks 
 
 
 
    
    
def check_email_exist(email):
    connection = sqlite3.connect('flask_sandy.db' , check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM  users WHERE email = ?;",[email])
    ##print("Fetching single row")
    record = cursor.fetchone()
    
    if record:
     ##print(record[1]) print fullname
     message=True;
    
    else:
    
     message = False;
    
    return message;    
    
    
    
def delete_user_with_tasks(user_id):
    """
    Delete all rows in the tasks table
    :param conn: Connection to the SQLite database
    :return:
    """
    connection = sqlite3.connect('flask_sandy.db' , check_same_thread = False)
    cursor = connection.cursor()
    ###delete user first
    try:
        cursor.execute("DELETE FROM  users WHERE user_id = ?;",[user_id])
        cursor.execute("DELETE FROM  tasks WHERE user_id = ?;",[user_id])
    
        connection.commit()
        print("Successfully Deleted user with associated tasks : ", cursor.rowcount)
        cursor.close()
   
    except sqlite3.Error as error:
        print("deletion of user with associated tasks error : ", error)
    finally:
     if connection:
        connection.close()
        
    
    return True;
    
    
    
    
    
    
def new_user(fname,email,password,ctime):

  try:
    connection = sqlite3.connect('flask_sandy.db' , check_same_thread = False)
    cursor = connection.cursor()
    sqlite_insert_query = """
    INSERT INTO users(
    fullname,
    email,
    password,
    timestamp
    ) VALUES(?,?,?,?);"""
    
    
    if check_email_exist(email):
       print("Email already taken. Please use a different email address.")
    
    else:
    
    
# This is the qmark style:
       
       new_user= cursor.execute(sqlite_insert_query,[fname,email,password,ctime])
    connection.commit()
    print("New user successfully added : ", cursor.rowcount)
    cursor.close()
   
  except sqlite3.Error as error:
    print("Failed to add new user : ", error)
  finally:
    if connection:
       connection.close()
        
    
