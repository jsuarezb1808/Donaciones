from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Integer,String,Boolean,DATE  
from config.db import meta,engine

Donaciones = Table("donaciones",meta, 
                   Column("UUID",String,primary_key=True),
                   Column("Nombre1",String(225)),
                   Column("Nombre2",String(225)),
                   Column("apellido1",String(225)),
                   Column("apellido2",String(225)),
                   Column("TipoDocumento",String(225)),
                   Column("NumDoc",String(225)),
                   Column("InteresDonacion",String(225)),
                   Column("AceptaTerminos",String(225)),
                   Column("Valor",String(225)),
                   Column("EstatusDonacion",String(225)),
                   Column("DonacionUpdate",DATE),
                )

meta.create_all(engine)