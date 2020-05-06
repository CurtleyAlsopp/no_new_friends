#!/usr/bin/python3

import mysql.connector as mydb


#Prompt users for credentials
db_uname = input("Provide DB username: ")
db_pword = input("Provide DB pword: ")

#Connect to MYSQL database
mydb_connnection = mydb.connect(
    user = db_uname,
    password = db_pword,
    database = "no_new_friends_db"
)

#Initialize cursor
cursor = mydb_connnection.cursor()


cursor.execute ("CREATE TABLE users(id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(30) NOT NULL UNIQUE, login_key VARCHAR(20));")
cursor.execute ( "CREATE TABLE messages(sender_user_id INT, FOREIGN KEY(sender_user_id) REFERENCES users(id), receiver_user_id INT, FOREIGN KEY(receiver_user_id) REFERENCES users(id), time_sent DATETIME, time_delivered DATETIME,message_delivered BOOLEAN, message VARCHAR(500) );" )
