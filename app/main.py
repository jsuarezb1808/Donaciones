from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from pydantic import BaseModel

class UserForm(BaseModel):
    primer_nombre: str
    segundo_nombre: str|None = None
    primer_apellido: str
    segundo_apellido: str|None = None

app=FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.post("/")
def handle_form_data(userForm: UserForm):
    print(userForm)

@app.get("/")
def get_form(request:Request):
    return templates.TemplateResponse(
        request=request, name="index.html")

@app.get("/test/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str,item:str,param: str|None=None):
    print ("params: ",request.query_params)
    print ("params: ",request.body)
    return templates.TemplateResponse(
        request=request, name="test.html", context={"id": id}
    )




