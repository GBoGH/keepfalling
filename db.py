import mysql.connector as conn

db = conn.connect(
    host="localhost",
    user="python",
    password="python",
    database="keepfalling"
)


def insert(table_name, UserName, LastScore, HighScore):
    cursor = db.cursor()
    querry = "INSERT INTO %s (UserName, LastScore, HighScore)" \
             "VALUES (%s, %d, %d)" \
             %(table_name, UserName, LastScore, HighScore)
    cursor.execute(querry)
    db.commit()

def bestx(table_name, n):
    names = ["HIGHSCORES",]
    cursor = db.cursor()
    querry = "SELECT UserName, HighScore " \
             "FROM %s " \
             "ORDER BY HighScore DESC " \
             "LIMIT %s" %(table_name, n)
    cursor.execute(querry)
    result = cursor.fetchall()
    for i in result:
        name = i[0]
        name = name.replace("'", "")
        score = i[1]
        names.append("%s   %d"%(name, score))
    return names

