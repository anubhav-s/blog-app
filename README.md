# blog-app

Following are the steps to deploy the application:

1. Clone the code from repository using following branch: git clone --branch master_change https://github.com/anubhav-s/blog-app.git
2. Go to the root directory, where manage.py is found.
3. Create tables for the models in the database:
   a. Run the commands - "python3 manage.py makemigrations blog"
   b. "python3 manage.py migrate blog"
   c. And finally, "python3 manage.py migrate"
   
4. Just to ensure everything is working fine, run the command "python3 manage.py runserver". This command will 
   start the webserver on your terminal/command prompt.
5. Now, go to the URL: http://127.0.0.1:8000/. You will the main page of the application and click on the '+' sign on the top 
   right corner to start writing a new blog. After writing save the blog by clicking on the "save" button.
6. To edit the blog, you can click on the blog link and then can click on the "edit" button.
