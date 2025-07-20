from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Store survey responses in memory (list of dicts)
responses = []

@app.route('/', methods=['GET', 'POST'])
def survey():
    if request.method == 'POST':
        response = {
            'name': request.form['name'],
            'age_group': request.form['age_group'],
            'favorite_color': request.form['favorite_color'],
            'satisfaction': request.form['satisfaction']
        }
        responses.append(response)
        return redirect(url_for('results'))
    return render_template('survey.html')

@app.route('/results/')
def results():
    age_filter = request.args.get('age_group')
    if age_filter:
        filtered = [r for r in responses if r['age_group'] == age_filter]
    else:
        filtered = responses
    return render_template('result.html', responses=filtered, age_filter=age_filter)

if __name__ == '__main__':
    app.run(debug=True)
