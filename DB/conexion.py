import mysql.connector
from mysql.connector.constants import CONN_ATTRS_DN
from mysql.connector.errors import Error

class Dao:
    def __init__(self):
        try:
            self.CONEXION=mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                password='your_pass',
                db='database_name',
                port='3306'
            )
            print(f'Servidor corriendo: {self.CONEXION.get_server_info()}')
        except Error as e:
            print(f'No se puedo establecer la conexion con el servidor {e}')

    def mostrarCursos(self):
        if self.CONEXION.is_connected():
            try:
                CURSOR = self.CONEXION.cursor()
                CURSOR.execute('SELECT * FROM curso;')
                cursos = CURSOR.fetchall()
                return cursos
            except Error as e:
                print(f'Error al obtener los datos {e}')

    def registrarCurso(self,curso):
        if self.CONEXION.is_connected():
            try:
                CURSOR = self.CONEXION.cursor()
                SQL=f'INSERT INTO curso (`codigo_curso`,`nombre_curso`,`credito_curso`) VALUE("{curso[0]}","{curso[1]}","{curso[2]}");'
                CURSOR.execute(SQL)
                self.CONEXION.commit()
            except Error as e:
                print(f'Error al escribir en la tabla {e}')

    def eliminarCurso(self,codigo):
        if self.CONEXION.is_connected():
            try:
                CURSOR=self.CONEXION.cursor()
                SQL=f'DELETE FROM curso WHERE `codigo_curso` = "{codigo}";'
                CURSOR.execute(SQL)
                self.CONEXION.commit()
            except Error as e:
                print(f'Error al eliminar el curso {e}')

    def actualizarCurso(self,curso):
        if self.CONEXION.is_connected():
            try:
                CURSOR=self.CONEXION.cursor()
                SQL=f'UPDATE curso SET `nombre_curso`="{curso[1]}",`credito_curso`="{curso[2]}" WHERE `codigo_curso`="{curso[0]}";'
                CURSOR.execute(SQL)
                self.CONEXION.commit()
            except Error as e:
                print(f'Error al actualizar los datos {e}')
