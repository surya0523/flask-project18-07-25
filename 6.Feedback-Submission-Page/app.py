from flask import Flask, render_template, request, redirect, url_for
from feedback_data import feedbacks

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    message = request.form['message']
    feedbacks.append({"name": name, "message": message})
    return redirect(url_for('thankyou'))

@app.route('/thankyou')
def thankyou():
    return render_template("thankyou.html")

@app.route('/feedbacks')
def show_feedbacks():
    return render_template("feedbacks.html", feedbacks=feedbacks)

if __name__ == '__main__':
    app.run(debug=True)
