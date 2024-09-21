from sqlalchemy import create_engine, MetaData

DBuser="root"
DBpassword="P4ssw0rd123*"

engine = create_engine("mysql+pymysql://user:passwor@localhost:3306/db")
meta=MetaData()
connection=engine.connect()

