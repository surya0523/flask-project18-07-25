from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample pets data
pets = [
    {
        "id": 1,
        "name": "Buddy",
        "type": "Dog",
        "age": "3 years",
        "image": "dog1.jpg",
        "description": "Friendly golden retriever."
    },
    {
        "id": 2,
        "name": "Mittens",
        "type": "Cat",
        "age": "2 years",
        "image": "cat1.jpg",
        "description": "Playful tabby cat."
    }
]

# Track adoptions (in-memory)
adopted_pets = set()

@app.route('/')
def index():
    return render_template('index.html', pets=pets, adopted=adopted_pets)

@app.route('/pet/<int:pet_id>')
def pet_detail(pet_id):
    pet = next((p for p in pets if p["id"] == pet_id), None)
    if not pet:
        return "Pet not found", 404
    return render_template('pet.html', pet=pet)

@app.route('/adopt/<int:pet_id>', methods=['GET', 'POST'])
def adopt(pet_id):
    pet = next((p for p in pets if p["id"] == pet_id), None)
    if not pet:
        return "Pet not found", 404

    if request.method == 'POST':
        # Here you could process adopter info
        adopted_pets.add(pet_id)
        return redirect(url_for('index', adopted='success'))

    return render_template('adopt.html', pet=pet)

if __name__ == '__main__':
    app.run(debug=True)
