from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Integer,String,Boolean,DATE  
from config.db import meta,engine
import uuid

Donaciones = Table("donaciones",meta, 
                   #Column("ID",String(36), nullable=False, unique=True, default=uuid.uuid4),
                   Column("ID",Integer, primary_key=True, autoincrement=True),
                   Column("Nombre1",String(225)),
                   Column("Nombre2",String(225)),
                   Column("Apellido1",String(225)),
                   Column("Apellido2",String(225)),
                   Column("TipoDocumento",String(225)),
                   Column("NumDoc",String(225)),
                   Column("InteresDonacion",String(225)),
                   Column("AceptaTerminos",String(225)),
                   Column("Valor",String(225)),
                   Column("EstatusDonacion",String(225)),
                   Column("DonacionUpdate",DATE),
                )

meta.create_all(engine)