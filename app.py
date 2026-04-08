from flask import Flask, render_template, request
import json

app = Flask(__name__)

def guardar_datos(nombre):
    try:
        with open("almacenamiento.json", "r") as archivo:
            datos = json.load(archivo)

    except:
        datos = []

    if nombre not in datos:
        datos.append(nombre)

    with open("almacenamiento.json", "w") as archivo:
        json.dump(datos, archivo)

@app.route("/", methods=["GET", "POST"])
def appm():
    if request.method == "POST":
        nombre = request.form["nombre"]
        guardar_datos(nombre)

    return render_template("app.html")

if __name__ == "__main__":
    app.run(debug=True)