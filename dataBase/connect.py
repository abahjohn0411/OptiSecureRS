from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

dbusername = os.getenv("dbusername")
dbport = os.getenv('dbport')
dbname = os.getenv('dbname')
dbhost = os.getenv('dbhost')
dbpassword = os.getenv('dbpassword')

print(dbusername, dbport, dbname, dbhost, dbpassword)

DATABASE_URL = f"mysql+pymysql://{dbusername}:{dbpassword}@{dbhost}:{dbport}/{dbname}"

engine= create_engine(DATABASE_URL)

session= sessionmaker(bind=engine)

Base= declarative_base()

def getdb():
    db=session()
    return db