from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample in-memory storage
expenses = []

@app.route('/')
def home():
    return redirect(url_for('list_expenses'))

@app.route('/add', methods=['GET', 'POST'])
def add_expense():
    if request.method == 'POST':
        expense = {
            "id": len(expenses) + 1,
            "title": request.form['title'],
            "amount": float(request.form['amount']),
            "category": request.form['category'],
            "note": request.form.get('note', '')
        }
        expenses.append(expense)
        return redirect(url_for('list_expenses'))
    return render_template('add_expense.html')

@app.route('/expenses')
def list_expenses():
    category = request.args.get('category')
    filtered = expenses
    if category:
        filtered = [e for e in expenses if e['category'].lower() == category.lower()]
    return render_template('expenses.html', expenses=filtered, selected_category=category)

@app.route('/expense/<int:expense_id>')
def expense_detail(expense_id):
    expense = next((e for e in expenses if e['id'] == expense_id), None)
    if not expense:
        return "Expense not found", 404
    return render_template('expense.html', expense=expense)

if __name__ == '__main__':
    app.run(debug=True)
