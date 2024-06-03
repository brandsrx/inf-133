from flask import render_template
def perfil(user):
    return render_template("profile.html",user=user)
def login():
    return render_template("login.html")
def registro():
    return render_template("registro.html")
def actualizar():
    return render_template("actualiar.html")
def usuarios():
    return render_template("usuarios.html")