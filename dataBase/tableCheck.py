from connect import getdb
from sqlalchemy import text

def list_tables():
    db = getdb()
    result = db.execute(text("SHOW TABLES;"))
    tables = result.fetchall()

    print("Tables in database:")
    for row in tables:
        print(row[0])

list_tables()