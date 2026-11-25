from flask import Flask
import random

app = Flask(__name__)

facts_list = [
    "La mayoría de las personas que sufren adicción tecnológica experimentan un fuerte estrés cuando se encuentran fuera del área de cobertura de la red o no pueden utilizar sus dispositivos.",
    "Según un estudio realizado en 2018, más del 50% de las personas de entre 18 y 34 años se consideran dependientes de sus smartphones.",
    "El estudio de la dependencia tecnológica es una de las áreas más relevantes de la investigación científica moderna.",
    "Según un estudio de 2019, más del 60% de las personas responden a mensajes de trabajo en sus smartphones en los 15 minutos siguientes a salir del trabajo.",
    "Una forma de combatir la dependencia tecnológica es buscar actividades que aporten placer y mejoren el estado de ánimo.",
    "Elon Musk afirma que las redes sociales están diseñadas para mantenernos dentro de la plataforma.",
    "Las redes sociales tienen aspectos positivos y negativos, y debemos ser conscientes de ambos."
]


@app.route("/")
def hello_world():
    return f"<p>{random.choice(facts_list)}</p>"


@app.route("/about")
def about():
    return "<h1>Eliana</h1>"


@app.route("/clase")
def clase():
    return """
    <h1>Clase Python Pro</h1>
    <h2>Diego Moreno</h2>
    <h2>Diego Santiago</h2>
    <h2>Gael</h2>
    <h2>Aiden</h2>
    <h2>Omar</h2>
    """


# NUEVA PÁGINA: LANZAMIENTO DE MONEDA
@app.route("/moneda")
def moneda():
    resultado = random.choice(["Cara 🪙", "Cruz 🪙"])
    return f"""
    <body style="background-color: lightblue; text-align: center;">
        <h1>¡Lanzamiento de moneda!</h1>
        <h2>{resultado}</h2>
        <p>Recarga la página para lanzar otra vez.</p>
    </body>
    """


# NUEVA PÁGINA: ADIVINANZA
@app.route("/adivinanza")
def adivinanza():
    return """
    <body style="background-color: lightyellow; text-align: center;">
        <h1>¡Una adivinanza! 🧩</h1>
        <h2>Cuanto más le quitas, más grande se vuelve.
        ¿Qué es?</h2>
        <p>¡Piensa bien la respuesta!</p>
        <details>
            <summary>Ver respuesta</summary>
            <h3>Un agujero 🕳️</h3>
        </details>
    </body>
    """


# NUEVA PÁGINA: SECRET
@app.route("/secret")
def secret():
    return """
    <body style="background-color: lavender; text-align: center;">
        <h1>¡Encontraste la página secreta! 🔐</h1>
        <h2>Python es un lenguaje increíble.</h2>
        <p>¡Sigue aprendiendo y creando proyectos!</p>
    </body>
    """


app.run(debug=True)
