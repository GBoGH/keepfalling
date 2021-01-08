import os

import mysql.connector as conn
from dotenv import load_dotenv

# Loading environemnt variables
load_dotenv()

# Getting environment variables from the file
name = os.environ.get("DATABASE_NAME")
username = os.environ.get("DATABASE_LOGIN")
password = os.environ.get("DATABASE_PASSWORD")

# Connection to the database
db = conn.connect(
    host="sql7.freesqldatabase.com",
    user=f"{username}",
    password=f"{password}",
    database=f"{name}",
)


# Querry to insert new score into table.
def insert(table_name, user_name, high_score):
    cursor = db.cursor()
    querry = "INSERT INTO %s (UserName, HighScore)" \
             "VALUES (%s, %d)" \
             % (table_name, user_name, high_score)
    cursor.execute(querry)
    db.commit()


# Querry to select x best scores and put them into a list.
def bestx(table_name, n):
    names = ["HIGHSCORES:", ]
    cursor = db.cursor()
    querry = "SELECT UserName, HighScore " \
             "FROM %s " \
             "ORDER BY HighScore DESC " \
             "LIMIT %s" % (table_name, n)
    cursor.execute(querry)
    result = cursor.fetchall()
    for i in result:
        name = i[0]
        name = name.replace("'", "")
        score = i[1]
        names.append(f"{name}   {score}")
    return names
