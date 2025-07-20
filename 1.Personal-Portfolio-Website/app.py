from flask import Flask, render_template, request, redirect, url_for
from data import projects

app = Flask(__name__)

@app.route('/')
def home():
    tag = request.args.get('tag')
    filtered_projects = [p for p in projects if tag in p["tags"]] if tag else projects
    return render_template("home.html", projects=filtered_projects)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # You can log or email this message!
        return redirect(url_for('success'))
    return render_template("contact.html")

@app.route('/success')
def success():
    return render_template("success.html")

@app.route('/project/<int:id>')
def project_detail(id):
    project = next((p for p in projects if p["id"] == id), None)
    return render_template("project_detail.html", project=project)

if __name__ == '__main__':
    app.run(debug=True)
