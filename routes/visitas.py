from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.encoders import jsonable_encoder
from fastapi import HTTPException, APIRouter, FastAPI, Request

from pathlib import Path

from config.db import connection
from models.donaciones import Donaciones
from schemas.visitas import UserForm

from datetime import datetime 

visitantes=APIRouter()

visitantes.mount("/static", StaticFiles(directory="static"), name="static")
BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(Path(BASE_DIR,'../templates')))
    
#ruta encargada de recibir la informacion del formulario
@visitantes.post("/")
async def Store_visitantes(userForm:UserForm):
    new_visita = {
        "actividad":userForm.actividad,
        "tipo_documento":userForm.tipo_documento,
        "numero_documento":userForm.numero_documento,
        "primer_nombre":userForm.primer_nombre,
        "segundo_nombre":userForm.segundo_nombre,
        "primer_apellido":userForm.primer_apellido,
        "segundo_apellido":userForm.segundo_apellido,
        "fecha_nacimiento":userForm.fecha_nacimiento,
        "genero":userForm.genero,
        "es_victima_conflicto_armado":userForm.es_victima_conflicto_armado,
        "pais":userForm.pais,
        "ciudad":userForm.ciudad,
        "comuna":userForm.comuna,
        "orientacion_sexual":userForm.orientacion_sexual,
        "discapacidad":userForm.discapacidad,
        "etnia":userForm.etnia,
        "organizacion":userForm.organizacion,
        "contactar_whatsapp":userForm.contactar_whatsapp,
        "contactar_correo":userForm.contactar_correo,
        "correo":userForm.correo,
        "telefono":userForm.telefono,
        "hacer_donacion":userForm.hacer_donacion,
        "terminos_condiciones":userForm.terminos_condiciones,
        "valor_donacion":userForm.valor_donacion
    }
    new_donacion={
        "Nombre1":new_visita["primer_nombre"],
        "Nombre2":new_visita["segundo_nombre"],
        "Apellido1":new_visita["primer_apellido"],
        "Apellido2":new_visita["segundo_apellido"],
        "TipoDocumento":new_visita["tipo_documento"],
        "NumDoc":new_visita["numero_documento"],
        "InteresDonacion":new_visita["hacer_donacion"],
        "AceptaTerminos":new_visita["terminos_condiciones"],
        "Valor":new_visita["valor_donacion"],
        "EstatusDonacion":"False",
        "DonacionUpdate":datetime.now()
    }
    resultado=connection.execute(Donaciones.insert(),new_donacion)
    connection.commit()
    print(resultado)


#ruta encargada de mostrar el formulario al usuario
@visitantes.get("/")
def get_visitantes(request:Request):
    return templates.TemplateResponse(
        request=request, name="index.html")


#direccion para re generar el PDF de la donacion especificada
#a peticion
#ACTUALMENTE SOLO MUESTRA LOS DATOS EN LA BASE DE DATOS
@visitantes.get("/visitantes/donacion")
def get_Donacion_Status(request:Request):
        print(connection.execute(Donaciones.select()).fetchall())
        return str("")
        
        
