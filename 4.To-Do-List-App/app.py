from flask import Flask, render_template, request, redirect, url_for
from tasks import tasks

app = Flask(__name__)

@app.route('/')
def home():
    completed_filter = request.args.get('completed')
    if completed_filter == 'true':
        filtered_tasks = [t for t in tasks if t["completed"]]
    elif completed_filter == 'false':
        filtered_tasks = [t for t in tasks if not t["completed"]]
    else:
        filtered_tasks = tasks
    return render_template("home.html", tasks=filtered_tasks)

@app.route('/add', methods=['POST'])
def add_task():
    title = request.form['title']
    new_id = max(t["id"] for t in tasks) + 1 if tasks else 1
    tasks.append({"id": new_id, "title": title, "completed": False})
    return redirect(url_for('home'))

@app.route('/delete/<int:id>')
def delete_task(id):
    global tasks
    tasks = [t for t in tasks if t["id"] != id]
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
