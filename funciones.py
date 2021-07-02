#---------METODOS GENERICOS----------
def validarTamanio(dato,tamaño):
    if len(dato)>tamaño:
        print(f'El dato no sebe ser mayor a {tamaño} caracteres, vuelva a ingresar')
        return False
    else:
        return True
#------METODOS ESPECIFICOS----------
def mostrarCursos(cursos):
    print('\n\n------------CURSOS---------------------')
    for curso in cursos:
        print(f'Codigo: {curso[1]} | Curso: {curso[2]}')
    print('-----------------------------------------')

def registarCurso():
    codigo=input('Ingrese codigo: ')
    while not(validarTamanio(codigo,10)):
        codigo=input('Ingrese codigo: ')
    curso=input('Ingrese curso: ')
    while not(validarTamanio(curso,30)):
        curso=input('Ingrese Curso: ')
    credito=input('Ingrese el credito: ')
    while not(validarTamanio(credito,3)):
        credito=input('Ingrese credito: ')
    CURSO=(codigo,curso,credito)
    return CURSO

def eliminarCurso(codigo,cursos):
    for curso in cursos:
        if curso[1]==codigo:
            return True
            break

def actualizarCurso(cursos,codigo):
    existe=False
    CURSO=()
    for curso in cursos:
        if curso[1]==codigo:
            existe=True
            curso=input('Actualizar curso: ')
            while not(validarTamanio(curso,30)):
                curso=input('Actualizar Curso: ')
            credito=input('Actualizar credito: ')
            while not(validarTamanio(credito,3)):
                credito=input('Actualizar credito: ')
            CURSO=(codigo,curso,credito)
            break
    return existe,CURSO
    