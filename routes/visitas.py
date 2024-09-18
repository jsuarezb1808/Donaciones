from fastapi import APIRouter

visitantes=APIRouter()

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
