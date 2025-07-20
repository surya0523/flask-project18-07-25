
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

weather_data = {
    "chennai": {"temp": "34°C", "status": "Sunny", "icon": "icons/sunny.png"},
    "delhi": {"temp": "29°C", "status": "Cloudy", "icon": "icons/cloudy.png"}
}

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        city = request.form.get("city").lower()
        return redirect(f"/weather/{city}")
    return render_template("home.html")

@app.route("/weather/<city>")
def show_weather(city):
    data = weather_data.get(city)
    if not data:
        return redirect("/error")
    return render_template("weather.html", city=city.title(), data=data)

@app.route("/error")
def error():
    return render_template("error.html")

if __name__ == "__main__":
    app.run(debug=True)
