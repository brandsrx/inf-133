from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from urllib.parse import urlparse,parse_qs
estudiantes = [
    {
        "id": 1,
        "nombre": "Pedrito",
        "apellido": "García",
        "carrera": "Ingeniería de Sistemas",
    },
    {
        "id": 2,
        "nombre": "Pedrito",
        "apellido": "García",
        "carrera": "Economia",
    },
    {
        "id": 3,
        "nombre": "María",
        "apellido": "López",
        "carrera": "Economia",
    }
]

class RESTRequestHandler(BaseHTTPRequestHandler):
    def responseHandler(self,statusCode,data):
        self.send_response(statusCode)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode('utf-8'))
        
    def do_GET(self):
        parsed_path = urlparse(self.path)
        query_params = parse_qs(parsed_path.query)
        if self.path == '/estudiantes':
            self.responseHandler(200,estudiantes)
        elif self.path == "/carreras":
            carreras = [estudiante["carrera"] for estudiante in estudiantes]
            self.responseHandler(200,carreras)
        elif self.path == "/estudiantes/economia":
            estudiantesEconomia = [estudiante for estudiante in estudiantes if estudiante["carrera"].lower() == "economia"]
            self.responseHandler(200,estudiantesEconomia)         
        elif self.path.startswith("/estudiantes/"):
            id = int(self.path.split("/")[-1])
            estudiante = next(
                (estudiante for estudiante in estudiantes if estudiante["id"] == id),
                None,
            )
            if estudiante:
                self.responseHandler(200,estudiante)

        elif self.path == "/contar_carreras":
            carreras = {}
            for estudiante in estudiantes:
                carrera = estudiante["carrera"]
                carreras[carrera] = carreras.get(carrera, 0) + 1
            self.responseHandler(200,carreras)
        elif self.path == "/total_estudiantes":
            total = len(estudiantes)
            self.responseHandler(200,{"total":total})
            
        else:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"Error": "Ruta no existente"}).encode('utf-8'))
            
    def do_POST(self):
        if self.path == '/estudiantes':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            post_data = json.loads(post_data.decode('utf-8'))
            post_data['id'] = len(estudiantes) + 1
            estudiantes.append(post_data)
            self.send_response(201)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(estudiantes).encode('utf-8'))
        elif self.path == "/estudiantes/economia":
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            post_data = json.loads(post_data.decode('utf-8'))
            post_data['id'] = len(estudiantes) + 1
            estudiantes.append(post_data)
            self.send_response(201)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(estudiantes).encode('utf-8'))
        else:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"Error": "Ruta no existente"}).encode('utf-8'))
    def find_student(self,id,estudiantes):
        return next(
                (estudiante for estudiante in estudiantes if estudiante["id"] == id),
                None,
            )
    def do_PUT(self):
        if self.path.startswith("/estudiantes/"):
            id = int(self.path.split("/")[-1])
            estudiante = self.find_student(id)
            data = self.read_data()
            if estudiante:
                estudiante.update(data)
                self.response_handler(200, [estudiantes])
            else:
                self.response_handler(404, {"Error": "Estudiante no encontrado"})
        else:
            self.response_handler(404, {"Error": "Ruta no existente"})
            
    def do_DELETE(self):
        if self.path == "/estudiantes":
            self.send_response(200)
            self.end_headers()
            self.send_header("Content-type", "application/json")
            estudiantes.clear()
            self.wfile.write(json.dumps(estudiantes).encode("utf-8"))
        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"Error": "Ruta no existente"}).encode("utf-8"))
def run_server(port = 8000):
    try:
        server_address = ('', port)
        httpd = HTTPServer(server_address, RESTRequestHandler)
        print(f'Iniciando servidor web en http://localhost:{port}/')
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('Apagando servidor web')
        httpd.socket.close()

if __name__ == "__main__":
    run_server()