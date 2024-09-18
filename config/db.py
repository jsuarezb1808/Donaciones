from sqlalchemy import create_engine, MetaData

DBuser="root"
DBpassword="P4ssw0rd123*"

engine = create_engine("mysql+pymysql://"+DBuser+":"+DBpassword+"@localhost:3306/mcmdonaciones")
meta=MetaData()
connection=engine.connect()

