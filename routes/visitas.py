from fastapi import APIRouter,Request
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path


visitantes=APIRouter()

visitantes.mount("/static", StaticFiles(directory="static"), name="static")
BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(Path(BASE_DIR,'../templates')))

class UserForm(BaseModel):
    primer_nombre: str
    segundo_nombre: str|None = None
    primer_apellido: str
    segundo_apellido: str|None = None
    
@visitantes.post("/")
def handle_form_data(userForm: UserForm):
    print(userForm)

@visitantes.get("/")
def get_form(request:Request):
    return templates.TemplateResponse(
        request=request, name="index.html")
