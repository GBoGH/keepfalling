import mysql.connector as conn

# Connection to the database
db = conn.connect(
    host="sql7.freesqldatabase.com",
    user="sql7385512",
    password="B368nrjnJb",
    database="sql7385512",
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
