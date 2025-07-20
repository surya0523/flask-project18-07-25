from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def get_letter_grade(score):
    score = float(score)
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

@app.route('/')
def home():
    return redirect(url_for('grade_form'))

@app.route('/grade', methods=['GET', 'POST'])
def grade_form():
    if request.method == 'POST':
        try:
            score = float(request.form['score'])
            return redirect(url_for('show_result', score=score))
        except ValueError:
            return render_template('form.html', error="Enter a valid number.")
    return render_template('form.html')

@app.route('/result')
def show_result():
    try:
        score = float(request.args.get('score', 0))
        letter = get_letter_grade(score)
        return render_template('result.html', score=score, letter=letter)
    except ValueError:
        return redirect(url_for('grade_form'))

if __name__ == '__main__':
    app.run(debug=True)
