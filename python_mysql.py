import pickle
import pymysql


with open("for_DBtest.txt", "rb")as c:
    text = pickle.load(c)
    
    
db = pymysql.connect("localhost","****","****","test", use_unicode=True, charset="utf8") #hostname, username, password, DBname
cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS PTT")

sql = """CREATE TABLE PTT (
         URL  CHAR(255) NOT NULL,
         DATE_1  CHAR(20),
         SOURCE_1 CHAR(20),
         BOARD_1 CHAR(50),
         TITLE_1 CHAR(100),
         AUTHOR_1 CHAR(200),  
         CORPUS_1 VARCHAR(10000) )"""

cursor.execute(sql)

count = 0
for i in text:
    url = i[0]
    date = i[1]
    source = i[2]
    board = i[3]
    title = i[4]
    author = i[5]
    corpus = i[6]
    sql = """INSERT INTO test.PTT(URL, \
    DATE_1, SOURCE_1, BOARD_1, TITLE_1, \
    AUTHOR_1, CORPUS_1) VALUES("%s", "%s", "%s", "%s", "%s", "%s", "%s")"""% \
    (url, date, source, board, title, author, corpus)
    
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        count += 1
        print(text.index(i))
print(count)

db.close()
