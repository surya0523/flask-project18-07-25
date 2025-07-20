from flask import Flask, render_template, request, redirect, url_for
from questions import questions

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        score = 0
        for q in questions:
            user_answer = request.form.get(f"q{q['id']}")
            if user_answer == q["answer"]:
                score += 1
        return redirect(url_for('result', score=score))
    return render_template("quiz.html", questions=questions)

@app.route('/result')
def result():
    score = request.args.get('score', type=int)
    return render_template("result.html", score=score, total=len(questions))

if __name__ == '__main__':
    app.run(debug=True)
