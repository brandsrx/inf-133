from http.server import HTTPServer
from pysimplesoap.server import SoapDispatcher, SOAPHandler

def saludar(nombre):
    return "¡Hola, {}!".format(nombre)
def SumaDosNumeros(x,y):
    return x+y
def CadenaPalindromo(cadena):
    cadena = cadena.replace(" ","").lower()
    return cadena==cadena[::-1]

dispatcher = SoapDispatcher(
    "ejemplo-soap-server",
    location="http://localhost:8000/",
    action="http://localhost:8000/",
    namespace="http://localhost:8000/",
    trace=True,
    ns=True,
)

dispatcher.register_function(
    "Saludar",
    saludar,
    returns={"saludo": str},
    args={"nombre": str},
)
dispatcher.register_function(
    "SumaDosNumeros",
    SumaDosNumeros,
    returns={"sumasdosnumeros": int},
    args={
        "x": int,
        "y":int
    },
)
dispatcher.register_function(
    "CadenaPalindromo",
    CadenaPalindromo,
    returns={"CadenaPalindromo": bool},
    args={"cadena": str},
)
server = HTTPServer(("0.0.0.0", 8000), SOAPHandler)
server.dispatcher = dispatcher
print("Servidor SOAP iniciado en http://localhost:8000/")
server.serve_forever()