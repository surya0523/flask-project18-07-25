from flask import Flask, render_template, request, redirect, url_for
from jobs import jobs

app = Flask(__name__)

@app.route('/')
def home():
    dept = request.args.get('dept')
    filtered = [j for j in jobs if j["dept"] == dept] if dept else jobs
    return render_template("home.html", jobs=filtered)

@app.route('/job/<int:id>')
def job_detail(id):
    job = next((j for j in jobs if j["id"] == id), None)
    return render_template("job_detail.html", job=job)

@app.route('/apply/<int:id>', methods=['GET', 'POST'])
def apply(id):
    job = next((j for j in jobs if j["id"] == id), None)
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        resume = request.form['resume']
        # You can store or email this data
        return redirect(url_for('success', title=job["title"]))
    return render_template("apply.html", job=job)

@app.route('/success')
def success():
    title = request.args.get('title')
    return render_template("success.html", title=title)

if __name__ == '__main__':
    app.run(debug=True)
