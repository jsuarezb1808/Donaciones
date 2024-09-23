from sqlalchemy import create_engine, MetaData

DBuser="root"
DBpassword="P4ssw0rd123*"

engine = create_engine("mysql+pymysql://user:password@127.0.0.1:3306/db")
meta=MetaData()
connection=engine.connect().execution_options(autocommit=True)


