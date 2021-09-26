# Flask based CRUD operations.

## Prerequisite
The following packages need to install to run the script.

    Flask == 2.0.1
    Flask-MySQLdb == 0.2.0

Use the following command to install packages.

    pip install package-name.
    
## Functionality
The following opertaions can be done with this application.

    * Modify
    * Delete

## Setting up the script
The following modifications need to change to execute the script successfully.

Step1:- Change the APP configuration in FLASK app.

   Configuring database App
   app.config['MYSQL_HOST'] = 'localhost'.
   
   app.config['MYSQL_USER'] = 'username'.
   
   app.config['MYSQL_PASSWORD'] = 'password'.
   
   app.config['MYSQL_DB'] = 'databasename'.
   
   mysql = MySQL(app).
   
Step2:- Use "MYSQL.info" and create the database.

Step3:- Use the following command to run flask applications.

    export FLASK_APP=app.py
    export FLASK_DEBUG=1  { Opational }
    flask run
   
Step4:- The following output will be look like below
Home Page
![Screenshot from 2021-09-26 18-56-16](https://user-images.githubusercontent.com/86065440/134810226-5d525b6c-6389-4b10-a6fa-f7b74207689e.png)

Update Page
![Screenshot from 2021-09-26 19-04-16](https://user-images.githubusercontent.com/86065440/134810282-89d6c6d0-68a0-44af-9e68-e20511626c6e.png)

Before modification, The 5th record contains the place information is "Hanging bangalow".

Updated Record Page
![Screenshot from 2021-09-26 19-05-15](https://user-images.githubusercontent.com/86065440/134810304-ea290615-ea9d-48a8-bcc0-33a21a1867c9.png)

After modification, The 5th record contains the place information is "Hanging Villa".



