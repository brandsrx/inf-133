from zeep import Client

client = Client("http://localhost:8000")

result = client.service.Saludar(nombre="Brandon")
result2 = client.service.SumaDosNumeros(x=5,y=3)
result3 = client.service.CadenaPalindromo(cadena="python")
print(result)
print(result2)
print(result3)