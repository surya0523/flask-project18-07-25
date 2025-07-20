from flask import Flask, render_template, request, redirect, url_for
from posts import posts

app = Flask(__name__)

@app.route('/')
def home():
    query = request.args.get('q')
    if query:
        filtered = [p for p in posts if query.lower() in p["title"].lower()]
    else:
        filtered = posts
    return render_template("home.html", posts=filtered)

@app.route('/post/<int:id>')
def post_detail(id):
    post = next((p for p in posts if p["id"] == id), None)
    return render_template("post_detail.html", post=post)

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        new_id = len(posts) + 1
        title = request.form['title']
        content = request.form['content']
        tags = request.form['tags'].split(',')
        posts.append({"id": new_id, "title": title, "content": content, "tags": tags})
        return redirect(url_for('home'))
    return render_template("admin.html")

if __name__ == '__main__':
    app.run(debug=True)
