from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print("Antes de llamar")
        result = func(*args,**kwargs)
        print(*args)
        print("Despues de llamar")
        return 
    return wrapper

@my_decorator 
def greet(name):
    """Funcion para saludar a alguien"""
    print(f"hola, {name}")
greet("Juan")

print(greet.__name__)
print(greet.__doc__)