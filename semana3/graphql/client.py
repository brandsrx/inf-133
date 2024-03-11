import requests

query = """
    {
        hello
        goodbye
    }
"""

url = 'http://localhost:8000/graphql'

response = requests.post(url, json={'query': query})
print(response.text)