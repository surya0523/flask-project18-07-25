from flask import Flask, render_template, request, redirect, url_for
from vote_data import vote_options

app = Flask(__name__)
app.jinja_env.globals.update(vote_options=vote_options)  # Make available globally (optional)

@app.route('/')
def home():
    return render_template("home.html", vote_options=vote_options)

@app.route('/vote', methods=['GET', 'POST'])
def vote_page():
    if request.method == 'POST':
        selected = request.form.get('option')
        if selected in vote_options:
            vote_options[selected]["votes"] += 1
            return redirect(url_for('results', selected=selected))
        return redirect(url_for('home'))
    return render_template("vote.html", vote_options=vote_options)

@app.route('/results')
def results():
    selected = request.args.get('selected')
    return render_template("results.html", options=vote_options, selected=selected)

if __name__ == '__main__':
    app.run(debug=True)
