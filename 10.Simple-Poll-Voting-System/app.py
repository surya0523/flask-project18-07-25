from flask import Flask, render_template, request, redirect, url_for
from poll_data import poll

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/poll', methods=['GET', 'POST'])
def poll_page():
    if request.method == 'POST':
        selected = int(request.form['option'])
        poll["votes"][selected] += 1
        return redirect(url_for('results', voted=selected))
    return render_template("poll.html", poll=poll)

@app.route('/results')
def results():
    voted = request.args.get('voted', type=int)
    return render_template("results.html", poll=poll, voted=voted)

if __name__ == '__main__':
    app.run(debug=True)
