import sqlite3

def SignupsWithTotalTasks():

    connection = sqlite3.connect('flask_sandy.db' , check_same_thread = False)
    cursor = connection.cursor()

## defining the Query
    query = "select (users.fullname) as fname, (users.email) as email,count(tasks.user_id) as totals from users left join tasks on (users.user_id = tasks.user_id);"

## getting records from the table
    cursor.execute(query)

## fetching all records from the 'cursor' object
    records = cursor.fetchone()
    
    if records == "None":
    
      tasks = ""
    
    else:
      tasks = records  
      
      return  tasks
    
