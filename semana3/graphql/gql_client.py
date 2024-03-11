import requests

query ="""
    {
        estudiantes{
            nombre
        }
    }
"""
query2 ="""
    {
        estudiantes{
            nombre
            apellido
        }
    }
"""

url ="http://localhost:8000/graphql"
response = requests.post(url,json={"query":query,})
print(response.text)
response = requests.post(url,json={"query":query2,})
print(response.text)

