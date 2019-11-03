import mysql.connector
import Credentials_for_database as cd

cnx = mysql.connector.connect(user=cd.Username, password=cd.Password,
                              host=cd.Server,
                              database=cd.Database_name)
mycursor = cnx.cursor()

def delete_table():
    table_name = "customers"
    mycursor.execute("DROP TABLE " + table_name)

def creat_table():
    mycursor.execute("""CREATE TABLE customers (Userid int NOT NULL AUTO_INCREMENT,
     Last_Name VARCHAR(255), 
     First_Name VARCHAR(255),
     email VARCHAR(255),
     password VARCHAR(255), 
     mobile int,
     photo int, 
     PRIMARY KEY (Userid))""")
    mycursor.execute("""CREATE TABLE expences (id int NOT NULL AUTO_INCREMENT,
     name VARCHAR(255), 
     purpose VARCHAR(255),
     date VARCHAR(255),
     time VARCHAR(255), 
     type VARCHAR(255),
     customer_id int, 
     PRIMARY KEY (id))""")
    mycursor.execute("CREATE TABLE sub_category(expence_type VARCHAR(255))")

creat_table()


cnx.close()

