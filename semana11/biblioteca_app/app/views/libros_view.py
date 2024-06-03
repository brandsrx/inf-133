from flask import render_template
def render_libro_list(libros):
    # Representa una lista de libroes como una lista de diccionarios
    return render_template("libro.html",libros=libros)


def render_libro_detail(libro):
    return render_template("libro.html",libro)
def create():
    return render_template("registro.html")
def update():
    return render_template("update_libro.html")