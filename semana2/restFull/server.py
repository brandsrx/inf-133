from http.server import HTTPServer, BaseHTTPRequestHandler
import json

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
    def do_GET(self):
        if self.path == '/estudiantes':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(estudiantes).encode('utf-8'))
        elif self.path == "/carreras":
            self.send_response(200)
            self.send_header("Content-type","application/json")
            self.end_headers()
            carreras = [estudiante["carrera"] for estudiante in estudiantes]
            self.wfile.write(json.dumps(carreras).encode("utf-8"))
        elif self.path == "/estudiantes/economia":
            self.send_response(200)
            self.send_header("Content-type","application/json")
            self.end_headers()
            estudiantesEconomia = [estudiante for estudiante in estudiantes if estudiante["carrera"].lower() == "economia"]
            self.wfile.write(json.dumps(estudiantesEconomia).encode("utf-8"))
            
        elif self.path.startswith("/estudiantes/"):
            id = int(self.path.split("/")[-1])
            estudiante = next(
                (estudiante for estudiante in estudiantes if estudiante["id"] == id),
                None,
            )
            if estudiante:
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(estudiante).encode("utf-8"))

        elif self.path == "/contar_carreras":
            self.send_response(200)
            self.send_header("Content-type","application/json")
            self.end_headers()
            carreras = {}
            for estudiante in estudiantes:
                carrera = estudiante["carrera"]
                carreras[carrera] = carreras.get(carrera, 0) + 1
            self.wfile.write(json.dumps(carreras).encode())
        elif self.path == "/total_estudiantes":
            self.send_response(200)
            self.send_header("Content-type","application/json")
            self.end_headers()
            total = len(estudiantes)
            self.wfile.write(json.dumps({"total":total}).encode())
            
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