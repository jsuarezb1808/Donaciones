from pydantic import BaseModel

class UserForm(BaseModel):
    actividad: str 
    tipo_documento: str
    numero_documento: str | None=None
    primer_nombre: str
    segundo_nombre: str| None=None
    primer_apellido: str
    segundo_apellido: str| None=None
    fecha_nacimiento: str| None=None
    genero: str| None=None
    es_victima_conflicto_armado: str| None=None
    pais: str| None=None
    ciudad: str| None=None
    comuna: str| None=None
    orientacion_sexual: str| None=None
    discapacidad: str| None=None
    etnia: str| None=None
    organizacion: str| None=None
    contactar_whatsapp: str| None=None
    contactar_correo: str| None=None
    correo: str| None=None
    telefono: str| None=None
    hacer_donacion: str| None=None
    terminos_condiciones: str| None=None
    valor_donacion: str|None=None
