from flask import Flask, render_template, request, redirect, url_for
from items import items

app = Flask(__name__)

@app.route('/')
def home():
    item_type = request.args.get('type')
    status = request.args.get('status')
    filtered = items
    if item_type:
        filtered = [i for i in filtered if i["type"] == item_type]
    if status:
        filtered = [i for i in filtered if i["status"] == status]
    return render_template("home.html", items=filtered)

@app.route('/item/<int:id>')
def item_detail(id):
    item = next((i for i in items if i["id"] == id), None)
    return render_template("item_detail.html", item=item)

@app.route('/add', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        new_id = max(i["id"] for i in items) + 1 if items else 1
        title = request.form['title']
        item_type = request.form['type']
        status = request.form['status']
        desc = request.form['desc']
        image = request.form['image']
        items.append({
            "id": new_id,
            "title": title,
            "type": item_type,
            "status": status,
            "desc": desc,
            "image": image
        })
        return redirect(url_for('confirm', title=title))
    return render_template("add_item.html")

@app.route('/confirm')
def confirm():
    title = request.args.get('title')
    return render_template("confirm.html", title=title)

if __name__ == '__main__':
    app.run(debug=True)
