from flask import Flask, render_template, request, redirect, url_for
from movies import movies, recommendations

app = Flask(__name__)

@app.route('/')
def home():
    genre = request.args.get('genre')
    filtered = [m for m in movies if m["genre"] == genre] if genre else movies
    return render_template("home.html", movies=filtered)

@app.route('/movie/<int:id>')
def movie_detail(id):
    movie = next((m for m in movies if m["id"] == id), None)
    return render_template("movie_detail.html", movie=movie)

@app.route('/recommend', methods=['GET', 'POST'])
def recommend():
    if request.method == 'POST':
        title = request.form['title']
        genre = request.form['genre']
        desc = request.form['desc']
        poster = request.form['poster']
        recommendations.append({
            "title": title,
            "genre": genre,
            "desc": desc,
            "poster": poster
        })
        return redirect(url_for('confirm', title=title))
    return render_template("recommend.html")

@app.route('/confirm')
def confirm():
    title = request.args.get('title')
    return render_template("confirm.html", title=title)

if __name__ == '__main__':
    app.run(debug=True)
