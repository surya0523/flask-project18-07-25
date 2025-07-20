from flask import Flask, render_template, request, redirect, url_for
from recipes import recipes

app = Flask(__name__)

@app.route('/')
def home():
    category = request.args.get('category')
    filtered = [r for r in recipes if r["category"] == category] if category else recipes
    return render_template("home.html", recipes=filtered)

@app.route('/recipe/<int:id>')
def recipe_detail(id):
    recipe = next((r for r in recipes if r["id"] == id), None)
    return render_template("recipe_detail.html", recipe=recipe)

@app.route('/add', methods=['GET', 'POST'])
def add_recipe():
    if request.method == 'POST':
        new_id = max(r["id"] for r in recipes) + 1 if recipes else 1
        title = request.form['title']
        category = request.form['category']
        desc = request.form['desc']
        image = request.form['image']  # image filename from static/images/
        recipes.append({
            "id": new_id,
            "title": title,
            "category": category,
            "desc": desc,
            "image": image
        })
        return redirect(url_for('home'))
    return render_template("add_recipe.html")

if __name__ == '__main__':
    app.run(debug=True)
