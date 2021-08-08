import sqlite3
from pprint import pprint

def tasks_diplay():

    connection = sqlite3.connect('flask_sandy.db' , check_same_thread = False)
    cursor = connection.cursor()

## defining the Query
    query = "SELECT * FROM tasks"

## getting records from the table
    cursor.execute(query)

## fetching all records from the 'cursor' object
    records = cursor.fetchall()
    
    if records == "None":
    
      tasks = ""
    
    else:
      tasks = records  
      
      return  tasks
      
      

def Mytasks_diplay(user_id):

    connection = sqlite3.connect('flask_sandy.db' , check_same_thread = False)
    cursor = connection.cursor()

## defining the Query
    query = "SELECT * FROM tasks where user_id=?"

## getting records from the table
    cursor.execute(query,[user_id])

## fetching all records from the 'cursor' object
    records = cursor.fetchall()
    
    if records == "None":
    
      tasks = ""
    
    else:
      tasks = records  
      
      return  tasks
            
      


def tasks_diplayWithUsers():

    connection = sqlite3.connect('flask_sandy.db' , check_same_thread = False)
    cursor = connection.cursor()

## defining the Query
    query = "SELECT * FROM tasks join users on tasks.user_id = users.user_id"

## getting records from the table
    cursor.execute(query)

## fetching all records from the 'cursor' object
    records = cursor.fetchall()
    
    if records == "None":
    
      tasks = ""
    
    else:
      tasks = records  
      
      return  tasks      
      
      

def tasks_diplayLimit5():

    connection = sqlite3.connect('flask_sandy.db' , check_same_thread = False)
    cursor = connection.cursor()

## defining the Query
    query = "SELECT * FROM tasks ORDER BY task_id DESC limit 5;"

## getting records from the table
    cursor.execute(query)

## fetching all records from the 'cursor' object
    records = cursor.fetchall()
    
    if records == "None":
    
      tasks = ""
    
    else:
      tasks = records  
      
      return  tasks
      

def Today_tasks():

    connection = sqlite3.connect('flask_sandy.db' , check_same_thread = False)
    cursor = connection.cursor()

## defining the Query
    query = 'SELECT * FROM tasks WHERE timestamp  >= datetime(\'now\', \'start of day\') ORDER BY task_id DESC;' 


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
          



def tasks_last_week():

    connection = sqlite3.connect('flask_sandy.db' , check_same_thread = False)
    cursor = connection.cursor()

## defining the Query
    query = 'SELECT * FROM tasks WHERE timestamp  BETWEEN datetime(\'now\', \'-6 days\') AND datetime(\'now\', \'localtime\') ORDER BY 	task_id DESC LIMIT 5;' 


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
    




def tasks_last_24hr():

    connection = sqlite3.connect('flask_sandy.db' , check_same_thread = False)
    cursor = connection.cursor()

## defining the Query
    query = 'SELECT * FROM tasks WHERE timestamp  > datetime(\'now\', \'-24 hour\') ORDER BY task_id DESC LIMIT 5;' 


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
    


def num_tasks():

    connection = sqlite3.connect('flask_sandy.db' , check_same_thread = False)
    cursor = connection.cursor()
## defining the Query
    query = "SELECT * FROM tasks ORDER BY task_id DESC"
## getting records from the table
    cursor.execute(query)
## fetching all records from the 'cursor' object
    records =len(cursor.fetchall())
    return  records 
  





def task_diplayID(id):

    connection = sqlite3.connect('flask_sandy.db' , check_same_thread = False)
    cursor = connection.cursor()

## defining the Query
    query = "SELECT * FROM tasks WHERE task_id=?"

## getting records from the table
    cursor.execute(query, [id])

## fetching all records from the 'cursor' object
    records = cursor.fetchone()
    
    if records == "None":
    
      tasks = ""
    
    else:
      tasks = records  
      
      return  tasks



    
def delete_all_tasks(conn):
    """
    Delete all rows in the tasks table
    :param conn: Connection to the SQLite database
    :return:
    """
    
    conn = sqlite3.connect('flask_sandy.db' , check_same_thread = False)
    sql = 'DELETE FROM tasks'
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit() 
    
    
def delete_task(id):
    """
    Delete a task by task id
    :param conn:  Connection to the SQLite database
    :param id: id of the task
    :return:
    """
    conn = sqlite3.connect('flask_sandy.db' , check_same_thread = False)
    sql = 'DELETE FROM tasks WHERE task_id=?'
    cur = conn.cursor()
    cur.execute(sql, [id])
    conn.commit()  
    
    
def updatetask(id,tname,tdescription):
    """
    UPDATE a task by task id
    :param conn:  Connection to the SQLite database
    :param id: id of the task
    :return:
    """
    conn = sqlite3.connect('flask_sandy.db' , check_same_thread = False)
    sql = 'UPDATE tasks SET task_name = ?,description = ?  WHERE task_id=?'
    cur = conn.cursor()
    cur.execute(sql, (tname,tdescription,id))
    conn.commit()     
        
    
    
    
def create(tname,tdescription,ctime,get_user_id):

  try:
    connection = sqlite3.connect('flask_sandy.db' , check_same_thread = False)
    cursor = connection.cursor()
    sqlite_insert_query = """
    INSERT INTO tasks(
    task_name,
    description,
    timestamp,
    user_id
    ) VALUES(
    ?,
    ?,
    ?,
    ?
    );"""
    
    new_user= cursor.execute(sqlite_insert_query,(tname,tdescription,ctime,get_user_id))
    connection.commit()
    notification = "New task successfully added:"
    cursor.close()
   
  except sqlite3.Error as error:
    notification = error 
  finally:
    if connection:
       connection.close()
        
  return  notification 
