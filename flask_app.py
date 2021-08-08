# A very simple Flask Hello World app for you to get started with...
from flask import Flask,render_template,request,session,redirect,url_for,flash
from flask_admin import Admin,BaseView, expose

import models.users
import models.tasks
import models.admin.users
import datetime




app = Flask(__name__)


app.secret_key = 'wrwerwr34534534te4rt454645tretger'



    #sess.init_app(app)

@app.route("/home" , methods =['GET'])
def home():
    """Return an HTML-formatted string and an optional response status code"""
    return """
      <!DOCTYPE html>
      <html>
      <head><title>My First Flask Application</title></head>
      <body><h1>hello world</h1></body>
      </html>
      """, 200

@app.route("/", methods =['GET','POST'])
def  index():
    if request.method == 'GET':
       
       return render_template('login.html',title='login'), 200
    else:


        username = request.form['username']
        password = request.form['password']

    if models.users.check_user(username,password):
    
    ##session manager
      session['username'] = username
      ##userID=models.users.get_userid(username)
      session['user_id'] =models.users.get_userid(username)
    
    ##session manager

       
      return redirect(url_for('dashboard'))
      
       #return render_template('dashboard.html', message = username, title='dashaboard',tasks= Test), 200
        
    else:
        error_message = "Incorrect username or password"
        return render_template('login.html', message = error_message,title='login'), 200


@app.route("/dashboard", methods =['GET'])
def dashboard():

    
 
    ##check if session is set else logout - start
    if 'username' in session:
    
        userlistreassign = models.users.UserReassignList(session['user_id'])
        #currenttask = models.tasks.tasks_diplay()
        currenttask = models.tasks.Mytasks_diplay(session['user_id'])
    
    
        return render_template('dashboard.html',title="Task List - Dashboard",tasks= currenttask,reassignUsers=userlistreassign), 200
    else:
    
        return redirect(url_for('logout'))
    ##check if session is set else logout - end
       

    
    
@app.route("/add_task", methods =['GET'])
def add_task():
    
      ##check if session is set else logout - start
    if 'username' in session:
    	return render_template('add_task.html',title='Add Task'), 200  
    
    else:
    
        return redirect(url_for('logout'))
    ##check if session is set else logout - end 
    
    
@app.route("/update_task", methods =['GET'])
def update_task():
   
    task_id = request.args.get('task')
    currenttask = models.tasks.task_diplayID(task_id)

    ##check if session is set else logout - start
    if 'username' in session:
    
        return render_template('update_task.html',title='Update Task page', html_task= currenttask), 200       
    
    else:
    
        return redirect(url_for('logout'))
    ##check if session is set else logout - end

 
@app.route("/taskupdateaction", methods =['POST'])
def taskupdateaction():

    Tname = request.form['tname']
    Tdescription = request.form['tdescription']

   ## task_id = request.args.get('task')
   
    
    models.tasks.updatetask(request.form['task_id'],Tname,Tdescription)
    
    return redirect(url_for('dashboard'))
    ##return render_template('add_task.html',title=task), 200  
 
 
 
 
    
@app.route("/taskdelete", methods =['GET'])
def taskdelete():

    task_id = request.args.get('task')
    
    models.tasks.delete_task(task_id)
    
    return redirect(url_for('dashboard'))
    ##return render_template('add_task.html',title=task), 200    
    
    
@app.route("/taskadd", methods =['POST'])
def taskadd():

    Tname = request.form['tname']
    Tdescription = request.form['tdescription']
    ctime=datetime.datetime.now()
    get_user_id=session['user_id'] 

    models.tasks.create(Tname,Tdescription,ctime,get_user_id)
    
    return redirect(url_for('dashboard'))
            
    



@app.route("/reassignTask", methods =['POST'])
def reassignTask():

        
 
    ##check if session is set else logout - start
    if 'username' in session:
    
        
        task_id = request.form['task_id']
        user_id  = request.form['user_id']
        userlistreassign = models.users.reassignTask(user_id,task_id)
        #currenttask = models.tasks.tasks_diplay()
        flash('Task successlly reassigned ')
    
    
        return redirect(url_for('dashboard'))
    else:
    
        return redirect(url_for('logout'))
    ##check if session is set else logout - end
       







@app.route("/logout", methods =['GET'])
def logout():
    
   session.clear()

   flash('logout successful')
   return redirect(url_for('index'))




@app.route("/about", methods =['GET'])
def about():

    return render_template('about.html',title='about',about_title ='About Company ABC',Team='Meet the team below'), 200
    
    
    
    


@app.route("/terms_conditions", methods =['GET'])
def terms_conditions():

    return render_template('terms_conditions.html',  message ="Terms and condition page" , title='Terms and Conditions'), 200



@app.route("/privacy", methods =['GET'])
def privacy():

    return render_template('Privacy.html' , message ="Privacy Statement page", title='privacy'), 200



@app.route("/registration", methods =['GET','POST'])
def registration():

    if request.method == 'GET':
       return render_template('registration.html',  message ="Registration page" , title='registration',note = "add new user"), 200
    else:
        fullname = request.form['fullname']
        username = request.form['username']
        password = request.form['password']
        ctime=datetime.datetime.now()
        
        ###register new user
        
        notification=models.users.new_user(fullname,username,password,ctime)
        
        return redirect(url_for('index'))
        
        



#admin = Admin(app)
# Add administrative views here
@app.route("/admin/login", methods =['GET','POST'])
def adminlogin():

    if request.method == 'GET':
      return render_template('admin/login.html' , message ="Admin -Login", title='Login Page | Materialize - Material Design'), 200

    else:


        username = request.form['username']
        password = request.form['password']

    if models.admin.users.check_user(username,password):
    
    ##session manager
      ##get user email
      session['useradmin'] = username
      ##get user_id
      session['user_id'] = models.admin.users.get_user_id(username)
      ##get user role
      session['user_role'] = models.admin.users.get_user_role(username)
    ##session manager

       
      return redirect(url_for('admin_dashboard'))
      
       #return render_template('dashboard.html', message = username, title='dashaboard',tasks= Test, user_id =), 200
        
    else:
        error_message = "Incorrect username or password"
        return render_template('admin/login.html' , message = error_message, title='Login Page | Materialize - Material Design'), 200


   
   

@app.route("/admin/", methods =['GET'])
def admin_dashboard():

   if 'user_id' in session:
   
     ctime=datetime.datetime.now()
     
     Current_username = models.admin.users.get_user_name(session['user_id'])
     TotalSignUps =models.users.TotalSignUps()
     TodaysTasks = models.tasks.Today_tasks()
     SigninUpsDisplay = models.users.SignUpsDisplayLimit5()
     TotalSignUpsLast24hrs=models.users.TotalSignUps_last_24hr()
     TotalSignUps_last_24hr_display = models.users.TotalSignUps_last_24hr_display()
     TodaySignsups=models.users.TodaySignUps()
     TasksLast24hrscount = len(models.tasks.tasks_last_24hr())
     TasksLast24hrs = models.tasks.tasks_last_24hr()
     TotalTasks = models.tasks.num_tasks()
     TaskdisplayLimit5 = models.tasks.tasks_diplayLimit5()
     TasksLast24hrsAll = models.tasks.tasks_last_24hr()
     TasksLastWeekAll = models.tasks.tasks_last_week()
     LastWeekSignupsAll = models.users.TotalSignUps_last_Week()
     now = datetime.datetime.now()
     date_now =now.strftime("%Y-%m-%d")
     d = datetime.timedelta(days = 6)
     LastWeekdate = now - d
     
     data = 							[TotalTasks,TotalSignUps,TasksLast24hrscount,TotalSignUpsLast24hrs,TodaysTasks,LastWeekdate,LastWeekSignupsAll,LastWeekdate,TasksLastWeekAll,TasksLast24hrs,TotalSignUps_last_24hr_display,SigninUpsDisplay,TaskdisplayLimit5,Current_username]
     

     return render_template('admin/dashboard.html',html_data =  data,title='Admin Dashboard', date_now =date_now ), 200   
   
   else:
    
    return redirect(url_for('adminlogin'))  
    
    
    
    
@app.route("/admin/users", methods =['GET'])
def admin_user_signups():

   if 'user_id' in session:
   
     
     Current_username = models.admin.users.get_user_name(session['user_id'])
     TotalSignUps =models.users.SignUpsDisplay()
     TotalTasks = models.tasks.num_tasks()
     TotalSignUpsnum=models.users.TotalSignUps()
     
     data = [Current_username,TotalSignUps,TotalTasks,TotalSignUps,TotalSignUpsnum ]
     

     return render_template('admin/user_signupsList.html',html_data =  data,title='Admin User SignUps'), 200   
   
   else:
    
    return redirect(url_for('adminlogin'))     
    
    
    
 
 
    
@app.route("/admin/tasks", methods =['GET'])
def admin_user_tasks():

   if 'user_id' in session:
   
     
     Current_username = models.admin.users.get_user_name(session['user_id'])
     TotalSignUps =len(models.users.SignUpsDisplay())
     TotalSignUpsnum = models.users.TotalSignUps()
     TotalTasksnum = len(models.tasks.tasks_diplayWithUsers())
     TotalTasks = models.tasks.tasks_diplayWithUsers()
     data = [Current_username,TotalSignUps,TotalTasksnum,TotalTasks ]
     

     return render_template('admin/user_tasksList.html',html_data =  data,title='Admin User Task Lists'), 200   
   
   else:
    
    return redirect(url_for('adminlogin'))      
    
    
    
    

@app.route("/admin/contacts", methods =['GET'])
def admin_contacts():

   if 'user_id' in session:
   
     
     Current_username = models.admin.users.get_user_name(session['user_id'])
     TotalSignUps =len(models.users.SignUpsDisplay())
     TotalSignUpsnum = models.users.TotalSignUps()
     TotalTasksnum = len(models.tasks.tasks_diplayWithUsers())
     TotalTasks = models.tasks.tasks_diplayWithUsers()
     data = [Current_username,TotalSignUps,TotalTasksnum,TotalTasks ]
     

     return render_template('admin/contacts.html',html_data =  data,title='Admin User Task Lists'), 200   
   
   else:
    
    return redirect(url_for('adminlogin'))      
    
       
    
    
    
    

@app.route("/admin/Viewtask", methods =['GET'])
def admin_viewtask():

   if 'user_id' in session:
     task_id = request.args.get('task')
     Get_task_details = models.tasks.task_diplayID(task_id)
     Current_username = models.admin.users.get_user_name(session['user_id'])
     TotalSignUps =len(models.users.SignUpsDisplay())
     TotalSignUpsnum = models.users.TotalSignUps()
     TotalTasksnum = len(models.tasks.tasks_diplayWithUsers())
     TotalTasks = models.tasks.tasks_diplayWithUsers()
     data = [Current_username,TotalSignUps,TotalTasksnum,TotalTasks,Get_task_details,task_id ]
     

     return render_template('admin/viewtask.html',html_data =  data,title='Admin User View Task'), 200   
   
   else:
    
    return redirect(url_for('adminlogin'))         
        
       
    
    
 
@app.route("/admin/ViewUser", methods =['GET'])
def admin_viewUser():

   if 'user_id' in session:
     user_id = request.args.get('user')
     Current_username = models.admin.users.get_user_name(session['user_id'])
     TotalSignUps =len(models.users.SignUpsDisplay())
     TotalTasksnum = len(models.tasks.tasks_diplayWithUsers())
     ViewUserDetails = models.users.user_details_diplayID(user_id)
     
     data = [Current_username,TotalSignUps,TotalTasksnum,ViewUserDetails]
     

     return render_template('admin/viewuser.html',html_data =  data,title='Admin View User details'), 200   
   
   else:
    
    return redirect(url_for('adminlogin')) 
    
    
    
 
@app.route("/admin/deleteUserWithTasks", methods =['GET'])
def admin_delete_user_with_tasks():

   if 'user_id' in session:
     user_id = request.args.get('id')
     
     #run deletion
     models.users.delete_user_with_tasks(user_id)
     
     return redirect(url_for('admin_user_signups'))
   
   else:
    
    return redirect(url_for('adminlogin'))       
      
     


@app.route("/admin/taskdelete", methods =['GET'])
def taskdelete_admin():

    task_id = request.args.get('task')
    
    models.tasks.delete_task(task_id)
    
    return redirect(url_for('admin_user_tasks'))
    ##return render_template('add_task.html',title=task), 200    
    



   
   
@app.route("/admin/logout", methods =['GET'])
def logoutadmin():
    
   session.clear()


   return redirect(url_for('adminlogin'))   
   
   
    


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
