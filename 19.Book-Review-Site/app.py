from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy data
books = [
    {"id": 1, "title": "Atomic Habits", "author": "James Clear", "cover": "covers/book1.jpg"},
    {"id": 2, "title": "Deep Work", "author": "Cal Newport", "cover": "covers/book2.jpg"}
]

reviews = {
    1: [{"name": "Alice", "rating": 5, "comment": "Life-changing!"}],
    2: [{"name": "Bob", "rating": 4, "comment": "Very useful."}]
}

@app.route('/')
def index():
    return render_template("index.html", books=books)

@app.route('/book/<int:book_id>', methods=['GET', 'POST'])
def book_detail(book_id):
    book = next((b for b in books if b["id"] == book_id), None)
    if not book:
        return "Book not found", 404

    if request.method == 'POST':
        name = request.form['name']
        rating = int(request.form['rating'])
        comment = request.form['comment']
        reviews.setdefault(book_id, []).append({"name": name, "rating": rating, "comment": comment})
        return redirect(url_for('book_detail', book_id=book_id))

    rating_filter = request.args.get('rating')
    all_reviews = reviews.get(book_id, [])
    if rating_filter:
        all_reviews = [r for r in all_reviews if str(r['rating']) == rating_filter]

    return render_template("book.html", book=book, reviews=all_reviews)

if __name__ == "__main__":
    app.run(debug=True)
