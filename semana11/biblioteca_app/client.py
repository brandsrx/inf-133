import requests

# URL base de la API
BASE_URL = "http://localhost:5000/api"

# Definir los encabezados de la solicitud
headers = {"Content-Type": "application/json"}

# Crear un nuevo animal
url = f"{BASE_URL}/libros"
nuevo_libro = {"titulo": "León2", "autor": "FelinoSasd", "edicion": "fiveSIx","disponibilidad":"si"}
response = requests.post(url, json=nuevo_libro, headers=headers)
print("\nCreando el segundo libro:")
print(response.json())

# Crear el segundo animal
nuevo_libro = {"titulo": "León", "autor": "Felino", "edicion": "five","disponibilidad":"NO"}
response = requests.post(url, json=nuevo_libro, headers=headers)
print("Creando un nuevo libro:")
print(response.json())

# Obtener la lista de todos los animales
url = f"{BASE_URL}/libros"
response = requests.get(url, headers=headers)
print("\nLista de animales:")
print(response.json())

# Obtener un animal específico por su ID (por ejemplo, ID=1)
url = f"{BASE_URL}/libros/1"
response = requests.get(url, headers=headers)
print("\nDetalles del animal con ID 1:")
print(response.json())

# Actualizar un animal existente por su ID (por ejemplo, ID=1)
url = f"{BASE_URL}/libros/1"
datos_actualizacion = {"titulo": "ac", "autor": "Fe213sd", "edicion": "15435Ix","disponibilidad":"sssssi"}
response = requests.put(url, json=datos_actualizacion, headers=headers)
print("\nActualizando el animal con ID 1:")
print(response.json())

# Eliminar un animal existente por su ID (por ejemplo, ID=1)
url = f"{BASE_URL}/libros/1"
response = requests.delete(url, headers=headers)
print("\nEliminando el animal con ID 1:")
if response.status_code == 204:
    print(f"Animal con ID 1 eliminado con éxito.")
else:
    print(f"Error: {response.status_code} - {response.text}")
