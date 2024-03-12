from http.server import HTTPServer,BaseHTTPRequestHandler
import json
from graphene import ObjectType,String,Int,List,Schema,Field


class Estudiante(ObjectType):
    id = Int()
    nombre = String()
    apellido = String()
    carrera = String()


class Query(ObjectType):
    estudiantes = List(Estudiante)
    estudiantes_por_carrera= Field(Estudiante,carrera=String())
    def resolve_estudiantes(root, info):
        return estudiantes
    def resolve_estudiantes_por_carrera(root,info,carrera):
        p = []
        for estudiante in estudiantes:
            if estudiante.carrera == carrera:
                p.append(estudiante)
        return p[1]
estudiantes = [
    Estudiante(
        id=1, 
        nombre="Pedrito",
        apellido="García", 
        carrera="Ingeniería de Sistemas"
    ),
    Estudiante(
        id=2,
        nombre="Jose",
        apellido="Lopez",
        carrera="Arquitectura"
    ),
    Estudiante(
        id=3, 
        nombre="Brandon",
        apellido="Mamani", 
        carrera="Ingeniería de Sistemas"
    ),
    Estudiante(
        id=4,
        nombre="Danner",
        apellido="Cruz",
        carrera="Arquitectura"
    ),
]

schema = Schema(query=Query)


class GraphQLRequestHandler(BaseHTTPRequestHandler):
    def response_handler(self, status, data):
        self.send_response(status)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))

    def do_POST(self):
        if self.path == "/graphql":
            content_length = int(self.headers["Content-Length"])
            data = self.rfile.read(content_length)
            data = json.loads(data.decode("utf-8"))
            result = schema.execute(data["query"])
            self.response_handler(200, result.data)
        else:
            self.response_handler(404, {"Error": "Ruta no existente"})


def run_server(port=3000):
    try:
        server_address = ("", port)
        httpd = HTTPServer(server_address, GraphQLRequestHandler)
        print(f"Iniciando servidor web en http://localhost:{port}/")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Apagando servidor web")
        httpd.socket.close()


if __name__ == "__main__":
    run_server()