# app.py
from flask import Flask, render_template, request, redirect, url_for
from models import session, Movie
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

@app.route('/')
def index():
    sort_by = request.args.get('sort_by')
    if sort_by == 'release_year':
        movies = session.query(Movie).order_by(Movie.release_year.desc()).all()
    elif sort_by == 'rating':
        movies = session.query(Movie).order_by(Movie.rating.desc()).all()
    else:
        movies = session.query(Movie).all()
    
    total_movies = session.query(Movie).count()
    watched_movies = session.query(Movie).filter_by(watched=True).count()
    unwatched_movies = session.query(Movie).filter_by(watched=False).count()

    return render_template('index.html', movies=movies, total_movies=total_movies, watched_movies=watched_movies, unwatched_movies=unwatched_movies)

@app.route('/add', methods=['GET', 'POST'])
def add_movie():
    if request.method == 'POST':
        title = request.form['title']
        release_year = request.form['release_year']
        genre = request.form['genre']
        rating = request.form['rating']
        watched = 'watched' in request.form

        new_movie = Movie(title=title, release_year=release_year, genre=genre, rating=rating, watched=watched)
        session.add(new_movie)
        session.commit()
        return redirect(url_for('index'))
    return render_template('add_movie.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_movie(id):
    movie = session.query(Movie).get(id)
    if request.method == 'POST':
        movie.title = request.form['title']
        movie.release_year = request.form['release_year']
        movie.genre = request.form['genre']
        movie.rating = request.form['rating']
        movie.watched = 'watched' in request.form
        session.commit()
        return redirect(url_for('index'))
    return render_template('edit_movie.html', movie=movie)

@app.route('/delete/<int:id>')
def delete_movie(id):
    movie = session.query(Movie).get(id)
    session.delete(movie)
    session.commit()
    return redirect(url_for('index'))

@app.route('/graphs')
def graphs():
    movies = session.query(Movie).all()

    # Graf po žanru
    genres = [movie.genre for movie in movies]
    genre_counts = {genre: genres.count(genre) for genre in set(genres)}
    plt.figure()
    plt.bar(genre_counts.keys(), genre_counts.values())
    plt.xlabel('Genre')
    plt.ylabel('Number of Movies')
    plt.title('Movies by Genre')
    genre_graph_path = os.path.join('static', 'genre_graph.png')
    plt.savefig(genre_graph_path)

    # Graf po ocjeni
    ratings = [movie.rating for movie in movies]
    plt.figure()
    plt.hist(ratings, bins=10, range=(0, 10))
    plt.xlabel('Rating')
    plt.ylabel('Number of Movies')
    plt.title('Movies by Rating')
    rating_graph_path = os.path.join('static', 'rating_graph.png')
    plt.savefig(rating_graph_path)

    # Graf po godini izlaska
    years = [movie.release_year for movie in movies]
    year_counts = {year: years.count(year) for year in set(years)}
    plt.figure()
    plt.bar(year_counts.keys(), year_counts.values())
    plt.xlabel('Year')
    plt.ylabel('Number of Movies')
    plt.title('Movies by Year')
    year_graph_path = os.path.join('static', 'year_graph.png')
    plt.savefig(year_graph_path)

    return render_template('graphs.html', genre_graph=genre_graph_path, rating_graph=rating_graph_path, year_graph=year_graph_path)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
