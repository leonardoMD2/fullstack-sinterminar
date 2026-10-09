from models import Estudiante
import sqlite3

class EstudiantesManager:
    def __init__(self):
        pass

    def agregarEstudiante(self, estudiante: Estudiante, conexion: sqlite3.Connection) -> str:
        conexion.execute("INSERT INTO estudiantes (nombre, apellido, img) VALUES (?,?,?)",(estudiante.nombre, estudiante.apellido, estudiante.img))
        return "Estudiante agregado"