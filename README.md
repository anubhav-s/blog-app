# blog-app

Following are the steps to deploy the application:

1. Clone the code from repository using - git clone https://github.com/anubhav-s/blog-app.git.
   There is pagination implemented in the following branch: git clone --branch master_change https://github.com/anubhav-s/blog-app.git
2. Go to the root directory.
3. Create tables for the models in the database:
   a. Run the commands - "python3 manage.py makemigrations blog"
   b. "python3 manage.py migrate blog"
   c. And finally, "python3 manage.py migrate"
   
4. Once you migrate the tables in sqllite database, create a super user using - "python3 manage.py createsuperuser"
   command. Fill in the details you want to fill in.
5. Just to ensure everything is working fine, run the command "python3 manage.py runserver". This command will 
   start the webserver on your terminal/command prompt.
6. Now go to web browser and paste this URL : http://127.0.0.1:8000/admin/. This should take you to admin console. Use the 
   credentials created at step 4 to login.
7. Now, go to the URL: http://127.0.0.1:8000/. You will the main page of the application and click on the '+' sign on the top 
   right corner to start writing a new blog. After writing save the blog by clicking on the "save" button.
8. To edit the blog, you can click on the blog link and then can click on the "edit" button.
