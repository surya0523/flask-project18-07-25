from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample dictionary with language support
dictionary_data = {
    'en': {
        'apple': 'A sweet red fruit.',
        'python': 'A high-level programming language.',
    },
    'es': {
        'apple': 'Una fruta roja dulce.',
        'python': 'Un lenguaje de programación de alto nivel.',
    }
}

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        word = request.form.get('word')
        lang = request.form.get('lang', 'en')
        return redirect(url_for('word_definition', word=word, lang=lang))
    return render_template('home.html')

@app.route('/word/')
def word_definition():
    word = request.args.get('word', '').lower()
    lang = request.args.get('lang', 'en')

    definition = dictionary_data.get(lang, {}).get(word)
    return render_template('word.html', word=word, definition=definition, lang=lang)

if __name__ == '__main__':
    app.run(debug=True)
