
from logging import error
from mysql.connector.errors import Error
from DB.conexion import Dao
import funciones


def menuPrincipal():
    continuar=True
    while continuar:
        print('######## MENU PRINCIPAL ############')
        print('1. Listar Cursos')
        print('2. Registrar Curso')
        print('3. Actualizar Curso')
        print('4. Eliminar Curso')
        print('5. Salir')
        print('####################################')
        opcion=int(input('Que desea realizar?      '))
        if opcion<1 or opcion>5:
            print('Opcion invalida, vuelva a ingresar nuevamente')
        elif opcion==5:
            print('Gracias por utilizar los servicios de FrankDev!!')
            continuar=False
        else:
            ejecutarOpcion(opcion)

def ejecutarOpcion(opcion):
    dao = Dao()
    if opcion==1:
        mostrar(dao)
    elif opcion==2:
        registar(dao)
    elif opcion==3:
        actualizar(dao)
    elif opcion==4:
        eliminar(dao)

def mostrar(dao):
    cursos=dao.mostrarCursos()
    if len(cursos)>0:
        funciones.mostrarCursos(cursos)
    else:
        print('Tabla vacia! no hay nada que mostrar\n\n')

def registar(dao):
    curso=funciones.registarCurso()
    dao.registrarCurso(curso)
    print('Curso registrado..!')

def eliminar(dao):
    cursos=dao.mostrarCursos()
    if len(cursos)>0:
        funciones.mostrarCursos(cursos)
        codigo=input('ingrese el codigo del curso a eliminar.    ')
        existe_curso=funciones.eliminarCurso(codigo,cursos)
        if existe_curso:
            dao.eliminarCurso(codigo)
            print('Curso eliminado..!')
        else:
            print('El codigo ingresado no se existe en los registros')
    else:
        print('Tabla vacia! No hay nada que eliminar\n\n')

def actualizar(dao):
    cursos=dao.mostrarCursos()
    if len(cursos)>0:
        funciones.mostrarCursos(cursos)
        codigo=input('Ingrese el codigo del curso a actualizar.!   ')
        existe_curso,CURSO=funciones.actualizarCurso(cursos,codigo)
        if existe_curso:
            dao.actualizarCurso(CURSO)
            print('Curso actualizado.!')
        else:
            print('El codigo ingresado no existe en los registros')
    else:
        print('Tabla vacia! nada que actualizar')
        
menuPrincipal()
