from flask import Flask,render_template
import requests

app = Flask(__name__)


@app.route("/<name>")
def guess(name):
    agi_URL = "https://api.agify.io/?name=" + name
    agi_response = requests.get(url=agi_URL)
    age = agi_response.json()["age"]

    gender_URL = "https://api.genderize.io?name=" + name
    gender_response = requests.get(url=gender_URL)
    gender = gender_response.json()["gender"]

    return render_template("index.html", name=name.title(), gender=gender, age=age)



if __name__ == ("__main__"):
    app.run(debug=True)

