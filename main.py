#from pj import stats
from json import decoder, load, dump
from time import sleep
from uuid import uuid4

#declaración de listas
alumnos = {
    'alumnos_creados':[]
}

docentes = {
    'docentes_creados':[]
}

#clases
class persona:#padre
    def __init__(self, nombre="") -> None:
        self.nombre = nombre

class alumno(persona):#hijo 1
    def __init__(self,nombre='', notas= [], notMay='', notMen='', notProm=''):
        super().__init__(nombre = nombre)
        self.notas = notas
        self.notMay = notMay
        self.notMen = notMen
        self.notProm = notProm

class docente(persona):#hijo 2
    def __init__(self, nombre='',edad='', dni=''):
        super().__init__(nombre=nombre)
        self.edad = edad
        self.dni = dni

def interfaz():# al tener self es un metodo de instancia para acceder a la clase
        while True:
            print('''
                Bienvenido al colegio,
                ¿Que deceas hacer?
                1) Gestionar Docentes
                2) Gestionar Alumnos
                3) Salir del programa\n ''')
            opcion  = input('> ')
            if opcion == "1":
                gest_doc()
            elif opcion == "2":
                gest_alu()
            elif opcion == "3":
                print("\n Gracias por usar la aplicación")
                sleep(1)
                quit()
            else:
                print("\nIntrodujiste una opion incorrecta")

#docente
def cargar_docentes():
    try:
        print("\n Docentes cargados...")
        archivo_doc = open("docentes.json", "r")
        docentes["docentes_creados"] = load(archivo_doc)
        archivo_doc.close()
    except FileNotFoundError:
        print("\n Creando registro de docentes...")
        archivo_doc = open("docentes.json", "w")
        archivo_doc.close()
    except decoder.JSONDecodeError:
        print("\n no hay docentes creados, se puede crear desde ahora")

def gest_doc():
    while True:
        print('''\n que deseas hacer: \n
                1) Ingresar nuevo docente
                2) Ver todos los docentes
                3) Volver al menu anterior''')

        raza = input("> ") 
        if raza == "1":
           nuevo_doc()

        elif raza == "2":
           listar_doc()
        elif raza =="3" :
            break
        else:
           print("\n Introdujiste una opcion erronea")

def nuevo_doc():
    nombre = input("\n Ingresa el nombre del Docente > ")
    edad = input("\n Ingresa la edad del Docente > ")#falta validar edad
    dni = input("\n Ingresa el dni del Docente > ")#falta validar DNI
    nuevoDoc = docente(nombre,edad,dni)
    datos = {
        "id" : str(uuid4),
        "nombre" : nuevoDoc.nombre,
        "edad" : nuevoDoc.edad,
        "dni" : nuevoDoc.dni
    }
    docentes['docentes_creados'].append(datos)
    pjs = docentes['docentes_creados']
    archivo = open("docentes.json", "w")
    dump(pjs,archivo, indent=4)
    archivo.close()

def listar_doc():
    for i in docentes['docentes_creados']:
        print('nombre: '+i["nombre"]+' Edad: '+i["edad"]+' DNI: '+i["dni"])
    

#Alumnos
def cargar_alumnos():
    try:
        print("\n Alumnos cargados...")
        archivo_alu = open("alumnos.json", "r")
        alumnos["alumnos_creados"] = load(archivo_alu)
        archivo_alu.close()
    except FileNotFoundError:
        print("\n Creando registro de alumnos...")
        archivo_alu = open("alumnos.json", "w")
        archivo_alu.close()
    except decoder.JSONDecodeError:
        print("\n no hay alumnos creados, se puede crear desde ahora")

def gest_alu():
    while True:
        print('''\n que deseas hacer: \n
                1) Ingresar nuevo alumno
                2) Ver todos los alumnos
                3) Volver al menu anterior''')

        raza = input("> ") 
        if raza == "1":
           nuevo_alu()

        elif raza == "2":
           listar_alu()
        elif raza =="3" :
            break
        else:
           print("\n Introdujiste una opcion erronea")

def nuevo_alu():
    notas = []
    nombre = input("\n Ingresa el nombre del Alumno > ")
    cant = int(input("\n cuantas notas ingresará > "))
        #Bucle for
    for i in range(cant):
        condi = 1
        #Bucle While, perciste hasta que la nota sea correcta y entre 0 y 20
        while True:
            # valida otro valor distinto de numero
            try:
                valor = float(input(f'ingrese la nota {i + 1}\n'))
            except ValueError:
                print('El dato ingresado no es número \n')
                continue
            
            #valida que se encuntre entre 0 y 20
            if valor > 20 or valor < 0:
                print('La nota ingresada es menor de cero o mayor a 20, por favor corregir \n')
                continue
            else:#ingresa valor a la lista
                notas.append(valor)
                break 


    nuevoAlu = alumno(nombre, notas, notMay = max(notas),notMen = min(notas), notProm = sum(notas)/len(notas))
    datos = {
        "id" : str(uuid4),
        "nombre" : nuevoAlu.nombre,
        "notas" : nuevoAlu.notas,
        "nota Mayor" : nuevoAlu.notMay,
        "nota Menor" : nuevoAlu.notMen,
        "nota Promedio" : nuevoAlu.notProm
    }
    alumnos['alumnos_creados'].append(datos)
    pjs = alumnos['alumnos_creados']
    archivo = open("alumnos.json", "w")
    dump(pjs,archivo, indent=4)
    archivo.close()

def listar_alu():
    print('entra metodo')
    for i in alumnos['alumnos_creados']:
        print(f'''nombre: {i["nombre"]} 
        notas: {i["notas"]} 
        Nota mayor: {i["nota Mayor"]} 
        Nota menor: {i["nota Menor"]} 
        Nota promedio: {i["nota Promedio"]} ''')

class Start:
    def __init__(self):
        try:
            cargar_docentes()
            cargar_alumnos()
            interfaz()
            
        except KeyboardInterrupt:
            print("\n Aplicación interrumpida")
Start()
