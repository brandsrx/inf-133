import requests

query ="""
    {
        estudiantesPorCarrera(carrera:"Arquitectura"){
            id
        }
    }
"""

url ="http://localhost:3000/graphql"
response = requests.post(url,json={"query":query,})
print(response.text)

