import requests
from flask import Flask, jsonify, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("hello.html")

# Déposez votre code à partir d'ici :

# ------------------------------
# Exercice 1 : Contact
# ------------------------------
@app.route("/contact")
def contact():
    return render_template("contact.html")


# ------------------------------
# Exercice 2 : API Paris
# ------------------------------
@app.get("/paris")
def api_paris():

    url = "https://api.open-meteo.com/v1/forecast?latitude=48.8566&longitude=2.3522&hourly=temperature_2m"

    response = requests.get(url)
    data = response.json()

    times = data.get("hourly", {}).get("time", [])
    temps = data.get("hourly", {}).get("temperature_2m", [])

    n = min(len(times), len(temps))

    result = [
        {
            "datetime": times[i],
            "temperature_c": temps[i]
        }
        for i in range(n)
    ]

    return jsonify(result)


# ------------------------------
# Exercice 3
# ------------------------------
@app.route("/rapport")
def rapport():
    return render_template("graphique.html")


# ------------------------------
# Exercice 5
# ------------------------------
@app.route("/histogramme")
def histogramme():
    return render_template("histogramme.html")


# ------------------------------
# Atelier
# ------------------------------
@app.get("/marseille")
def api_marseille():
    url = "https://api.open-meteo.com/v1/forecast?latitude=43.2965&longitude=5.3698&hourly=wind_speed_10m"
    response = requests.get(url)
    data = response.json()

    times = data.get("hourly", {}).get("time", [])
    winds = data.get("hourly", {}).get("wind_speed_10m", [])

    result = []
    for i in range(min(len(times), len(winds))):
        result.append({
            "datetime": times[i],
            "wind_speed": winds[i]
        })

    return jsonify(result)

@app.route("/atelier")
def atelier():
    return render_template("atelier.html")

# Ne rien mettre après ce commentaire

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
