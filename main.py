from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.utils import secure_filename
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

comentarios = []

# Create a directory for the uploaded images
UPLOAD_FOLDER = 'static/uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('feed'))
    return render_template('login.html')

@app.route('/feed', methods=['GET', 'POST'])
def feed():
    if 'username' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        comentario = request.form['comentario']
        if len(comentario) > 280:
            flash('your post is too long...')
            return redirect(url_for('feed'))
        if not comentario.strip():
            flash('Your post cannot be empty')
            return redirect(url_for('feed'))
        file = request.files['file']
        filename = None
        if file and file.filename != '':
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
        if comentario or filename:
            post = {
                'username': session['username'],
                'comentario': comentario,
                'filename': filename,
                'likes': 0,
                'comments': []
            }
            comentarios.append(post)

    return render_template('feed.html', comentarios=comentarios)

@app.route('/like/<int:post_id>', methods=['POST'])
def like(post_id):
    if 'username' not in session:
        return redirect(url_for('login'))

    post = comentarios[post_id]
    post['likes'] += 1

    return redirect(url_for('feed'))

@app.route('/comment/<int:post_id>', methods=['POST'])
def comment(post_id):
    if 'username' not in session:
        return redirect(url_for('login'))

    post = comentarios[post_id]
    comment = request.form['comment']
    post['comments'].append((session['username'], comment))

    return redirect(url_for('feed'))

if __name__ == '__main__':
    app.run(debug=True)

