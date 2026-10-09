from fastapi import FastAPI, Depends
from conexion import getConexion, initDb
from sqlite3 import Connection
from models import Estudiante
from manager.estudiantesManager import EstudiantesManager
from fastapi.middleware.cors import CORSMiddleware

estudiantesManager = EstudiantesManager()



app = FastAPI()


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Evento especifico que se ejecuta al iniciar la API
@app.on_event("startup")
def startup():
    initDb()


@app.get("/")
def root():
    return "Hola desde FastAPI"

@app.post("/agregar_estudiante")
def agregarEstudiante(estudiante: Estudiante, conexion: Connection = Depends(getConexion)):
    return estudiantesManager.agregarEstudiante(estudiante, conexion)

@app.get("/obtener_estudiantes")
def leerEstudiantes(nombre: str | None = None ,conexion: Connection = Depends(getConexion)):
    
    if nombre:
        return conexion.execute("SELECT * FROM estudiantes WHERE nombre = ?",(nombre,)).fetchone()
    
    res = conexion.execute("SELECT * FROM estudiantes").fetchall()
    return [dict(item) for item in res]


@app.get("/obtener_estudiantes/{id}")
def leerEstudiantes(id:int, conexion: Connection = Depends(getConexion)):
    res = conexion.execute("SELECT * FROM estudiantes WHERE id = ?",(id,)).fetchone()
    return res

@app.delete("/eliminar_estudiante/{id}")
def eliminarEstudiante(id: int, conexion: Connection = Depends(getConexion)):
    conexion.execute("DELETE FROM estudiantes WHERE id = ?",(id,))
    return "Estudiante eliminado"

# 1ro. Crear entorno virtual y activarlo
# para crear el entorno en linux: python3 -m venv env
# Activar entorno linux: source env/bin/activate
# 2do. Instalar dependencias con pip install "fastapi[standard]"
# 3ro. El codigo de arriba genera una api funcional
# 4to. Para correr la api fastapi dev main.py