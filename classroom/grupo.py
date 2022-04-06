from classroom.asignatura import Asignatura
from classroom.asignatura import Asignatura


class Grupo:

    grado = 12
    listadoAlumnos=[]
    def __init__(self, grupo="grupo predeterminado", asignaturas=None, estudiantes=None):
        self._grupo = grupo
        self._asignaturas=asignaturas
        self._estudiantes=estudiantes
    def __str__(self):
        cadena="Grupo de estudiantes: "+self._grupo
        return cadena

    def listadoAsignaturas(self, **kwargs):
        self._asignaturas=[]
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista=None):
        self.lista=lista
    #def agregarAlumno(self, alumno, listadoAlumnos=None):
        if(lista is None):
             self.listadoAlumnos = [alumno]
        else:
            self.listadoAlumnos = [alumno]
            self.listadoAlumnos = self.listadoAlumnos + self.lista
            #self.listadoAlumnos.append(alumno)
            #self.lista=[]
            #self.lista.append(alumno)
            #self.listadoAlumnos = self.listadoAlumnos + self.lista
    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre

