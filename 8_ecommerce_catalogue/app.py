
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

products = [
    {"id": 1, "name": "Laptop", "price": 50000, "image": "images/laptop.png"},
    {"id": 2, "name": "Headphones", "price": 1500, "image": "images/headphones.png"}
]

@app.route('/')
def index():
    return render_template("index.html", products=products)

@app.route('/product/<int:id>')
def product_detail(id):
    product = next((p for p in products if p["id"] == id), None)
    return render_template("product.html", product=product)

@app.route('/cart')
def cart():
    item_ids = request.args.getlist("id", type=int)
    items = [p for p in products if p["id"] in item_ids]
    return render_template("cart.html", items=items)

@app.route('/add-to-cart', methods=["POST"])
def add_to_cart():
    product_id = request.form.get("product_id")
    return redirect(url_for("cart", id=product_id))

if __name__ == '__main__':
    app.run(debug=True)
