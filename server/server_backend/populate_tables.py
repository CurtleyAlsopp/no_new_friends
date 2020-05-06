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



sql_code = "INSERT INTO users (username,login_key) VALUES (%s,%s)"
values_to_insert = [
    ('rcoombs','zdhfg4545'),
    ('kawai','okjghvbht574'),
    ('drawlins','dfghdrf25ff5d'),
    ('hpascall','243534ytrhgrs3r')
]

cursor.executemany(sql_code,values_to_insert)
mydb_connnection.commit()
