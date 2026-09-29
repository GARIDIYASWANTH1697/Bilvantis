# import mysql.connector

# print("MySQL connector installed successfully")


# import mysql.connector

# # Connect Python to MySQL
# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="your_mysql_password",
#     database="python_db"
# )

# if mydb.is_connected():
#     print("Database connected successfully!")

# mydb.close()



# import mysql.connector

# mydb = mysql.connector.connect(
#     host="localhost",
#     port=3306,
#     user="root",
#     password="YOUR_ACTUAL_PASSWORD",
#     database="python_db"
# )

# if mydb.is_connected():
#     print("Database connected successfully!")

# mydb.close()



# import mysql.connector

# mydb = mysql.connector.connect(
#     host="localhost",
#     port=3306,
#     user="root",
#     password="YOUR_ACTUAL_PASSWORD"
# )

# print("Connected successfully!")

# mydb.close()


import mysql.connector
from getpass import getpass

password = getpass("Enter MySQL password: ")

mydb = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password=password,
    database="python_db"
)


print("Database connected successfully!")

mydb.close()

