from pydantic import BaseModel
class Estudiante(BaseModel):
    nombre: str
    apellido: str
    img: str