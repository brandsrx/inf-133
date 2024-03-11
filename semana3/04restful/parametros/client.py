import requests
url = "http://localhost:8000/"
def MostrarCarreras():
    ruta_get = url+"carreras"
    get_response = requests.request(method="GET",url=ruta_get)
    print(get_response.text)
def MostrarEstudiantesEconomia():
    ruta_get = url+"estudiantes/economia"
    get_response = requests.request(method="GET",url=ruta_get)
    print(get_response.text)
def AgregarEstudiantesEconomia():
    nombre = input("Escriba el nombre:")
    apellido = input("Escriba el apellido:")
    nuevo_estudiante = {
        "nombre":nombre,
        "appellido":apellido,
        "carrera":"Economia"
    }
    post_response = requests.request(method="POST",url=url+"estudiantes/economia",json=nuevo_estudiante)
    print(post_response.text)
while True:
    print("------------------------------------------")
    print("Que desea realizar?")
    print("1):Mostrar todas las carreras\n"+
        "2):Estudiantes de la carrera de Economía\n"+
        "3):Agregar estudiantes de economia\n"+
        "4) salir")
    print("------------------------------------------")
    opc = int(input("Opcion: "))
    if(opc == 1):
        MostrarCarreras()
    elif(opc == 2):
        MostrarEstudiantesEconomia()
    elif(opc==3):
        AgregarEstudiantesEconomia()
    else:
        print("Bye bye")
        break
        