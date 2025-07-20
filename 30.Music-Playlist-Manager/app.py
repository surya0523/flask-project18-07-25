
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

playlists = [
    {'id': 1, 'name': 'Pop Hits', 'genre': 'pop', 'cover': 'pop.jpg', 'songs': ['Blinding Lights', 'Levitating']},
    {'id': 2, 'name': 'Rock Anthems', 'genre': 'rock', 'cover': 'rock.jpg', 'songs': ['Bohemian Rhapsody', 'Numb']},
]

@app.route('/')
def index():
    genre = request.args.get('genre')
    if genre:
        filtered = [p for p in playlists if p['genre'] == genre]
    else:
        filtered = playlists
    return render_template('index.html', playlists=filtered)

@app.route('/playlist/<int:playlist_id>', methods=['GET', 'POST'])
def playlist(playlist_id):
    playlist = next((p for p in playlists if p['id'] == playlist_id), None)
    if not playlist:
        return "Playlist not found", 404
    if request.method == 'POST':
        new_song = request.form['song']
        if new_song:
            playlist['songs'].append(new_song)
        return redirect(url_for('playlist', playlist_id=playlist_id))
    return render_template('playlist.html', playlist=playlist)

if __name__ == '__main__':
    app.run(debug=True)
