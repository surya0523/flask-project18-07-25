from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory list for demo
destinations = [
    {"name": "Paris", "region": "Europe", "image": "paris.jpg"},
    {"name": "Bali", "region": "Asia", "image": "bali.jpg"},
    {"name": "New York City", "region": "America", "image": "nyc.jpg"},
]

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('name')
        region = request.form.get('region')
        image = request.form.get('image')  # just filename
        destinations.append({"name": name, "region": region, "image": image})
        return redirect(url_for('destination_list'))
    return render_template('home.html')

@app.route('/destination/')
def destination_list():
    region_filter = request.args.get('region')
    if region_filter:
        filtered = [d for d in destinations if d["region"] == region_filter]
    else:
        filtered = destinations
    return render_template('destination.html', destinations=filtered, region_filter=region_filter)

if __name__ == '__main__':
    app.run(debug=True)
