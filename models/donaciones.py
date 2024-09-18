from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Integer,String,Boolean,DATE  
from config.db import meta

Donaciones = Table("donaciones",meta, 
                   Column("UUID",Integer,primary_key=True),
                   Column("Nombre1",String),
                   Column("Nombre2",String),
                   Column("apellido1",String),
                   Column("apellido2",String),
                   Column("TipoDocumento",String),
                   Column("NumDoc",String),
                   Column("InteresDonacion",Boolean),
                   Column("AceptaTerminos",Boolean),
                   Column("Valor",Integer),
                   Column("EstatusDonacion",Boolean),
                   Column("DonacionUpdate",DATE),
                )

