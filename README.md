# dashboard-django-vue

## Setup the project

* First, clone the project
  - Clone the repo by opening the terminal
  ```
    git clone https://github.com/hardikv21/dashboard-django-vue.git
  ```
  - Open IDE from that cloned folder

* Second, install dependencies and run the backend
  - After opening the IDE, open terminal from that path, and run the commands
  ```
    cd .\backend\
    pip install -r requirements.txt
  ```
  - Then create ".env" file in the same level with 2 variables: "SECRET_KEY", "PASSWORD"
  - To get value for secret key, run below command and copy and paste the value
  ```
    python -c "import secrets; print(secrets.token_urlsafe())"
  ```
  - For the password, follow the "Third, set the database" step
  - Lastly, run these commands to run the server correctly
  ```
    python .\manage.py migrate
    python .\manage.py runserver 
  ```
  - To run the test cases, run this command
  ```
    python .\manage.py test
  ```

* Third, set the database
  - Install postgreSQL using its documentation with pgAdmin - https://www.postgresql.org/
  - After that create the database with a name "dashboardDB" and desired password and also copy that password to the ".env" file, "PASSWORD" field
  - Make sure this database uses "5432" port while running
  - Once database created, use dump which is located at the root level of the "backend" folder with the name "backup" to restore the data
  - Follow this instructions to restore the data in pgAdmin - https://www.pgadmin.org/docs/pgadmin4/development/restore_dialog.html

* Forth, open "index.html" file from the frontend folder

## Once the setup is done, you will get this view in the browser

* User tab
![Screenshot 2022-09-22 173430](https://user-images.githubusercontent.com/43430462/191855714-8751a685-419f-4fa3-9501-4b311b1aa3c8.png)
  
  - By clicking on the any Name of the user,
  ![Screenshot 2022-09-22 173841](https://user-images.githubusercontent.com/43430462/191856142-ce99dc13-50f5-4d63-9c14-fabda217b690.png)

  - By clicking on the any Firm of the user,
  ![Screenshot 2022-09-22 174017](https://user-images.githubusercontent.com/43430462/191856369-a6246ab3-7ae1-4dbc-92da-64b67cd12231.png)

* Transaction tab
![Screenshot 2022-09-22 173647](https://user-images.githubusercontent.com/43430462/191855932-629109c0-771b-4aed-8a27-7aa4ed068070.png)

  - By clicking on the any Product of the transaction,
  ![Screenshot 2022-09-22 174202](https://user-images.githubusercontent.com/43430462/191856552-e442a4d1-2fed-4c25-a310-cb975484b1c6.png)

