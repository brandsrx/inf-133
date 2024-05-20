from flask import render_template
def create():
    return render_template("create_dulces.html")
def dulces(dulces):
    return render_template("dulces.html")
def actualizar(dulce):
    return render_template("actualiar.html")
    