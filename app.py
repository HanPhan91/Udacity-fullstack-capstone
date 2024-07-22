import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, Movie, Actor
from auth import AuthError, requires_auth


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    CORS(app)
    CORS(app, resources={r'/api/*': {'origins': '*'}})
    setup_db(app)

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'ContentType,Authorization, True')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET,POST,PUT,DELETE,UPDATE,OPTIONS')
        return response

    @app.route('/')
    def get_greeting():
        greeting = "!!!!! This is Final Project."
        return greeting

    @app.route('/movies', methods=['GET'])
    @requires_auth('view:movies')
    def get_all_movies(jwt):
        movies = Movie.query.all()

        moviesResponse = [movie.format() for movie in movies]
        return jsonify({
            'status': True,
            'message': 'Get movies successfully',
            'movies': moviesResponse
        })

    @app.route('/movies/add', methods=['POST'])
    @requires_auth('add:movies')
    def add_movie(jwt):
        body = request.get_json()
        title = body.get('title')
        release_year = body.get('release_year')

        if not title or not release_year:
            abort(422)
        try:
            movie = Movie(title=title, release_year=release_year)
            movie.insert()
            return jsonify({
                'status': True,
                'message': 'Add movie successfully',
                'movie': movie.format()
            })
        except BaseException as e:
            print(e)
            abort(422)

    @app.route('/movies/<int:movie_id>/update', methods=['PATCH'])
    @requires_auth('update:movies')
    def update_movie(jwt, movie_id):
        movie = Movie.query.get(movie_id)
        if not movie:
            abort(404)

        try:
            body = request.get_json()
            title = body.get('title')
            release_year = body.get('release_year')
            if not title or not title:
                abort(422)
            movie.title = title
            movie.release_year = release_year
            movie.update()
            return jsonify({
                'status': True,
                'message': 'Update movie successfully',
                'movie': movie.format()
            })
        except BaseException as e:
            print(e)
            abort(422)

    @app.route('/movies/<int:movie_id>/delete', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_movie(jwt, movie_id):
        movie = Movie.query.get(movie_id)
        if not movie:
            abort(404)
        try:
            movie.delete()
            return jsonify({
                'status': True,
                'message': 'Delete movie successfully',
                'movie_id': movie_id
            })
        except BaseException as e:
            print(e)
            abort(422)

    @app.route('/actors', methods=['GET'])
    @requires_auth('view:actors')
    def get_actors(jwt):
        actors = Actor.query.all()
        actorsResponse = [actor.format() for actor in actors]
        return jsonify({
            'status': True,
            'message': 'Get actors successfully',
            'actors': actorsResponse
        })

    @app.route('/actors/add', methods=['POST'])
    @requires_auth('add:actors')
    def add_actor(jwt):
        body = request.get_json()
        name = body.get('name')
        age = body.get('age')
        gender = body.get('gender')
        movie_id = body.get('movie_id')
        if not name or not age or not gender or not movie_id:
            abort(422)
        try:
            actor = Actor(name=name, age=age, gender=gender, movie_id=movie_id)
            actor.insert()
            return jsonify({
                'status': True,
                'message': 'Add actor successfully',
                'actor': actor.format()
            })
        except BaseException as e:
            print(e)
            abort(422)

    @app.route('/actors/<int:actor_id>/update', methods=['PATCH'])
    @requires_auth('update:actors')
    def update_actor(jwt, actor_id):
        actor = Actor.query.get(actor_id)
        if not actor:
            abort(404)

        try:
            body = request.get_json()
            name = body.get('name')
            age = body.get('age')
            gender = body.get('gender')
            movie_id = body.get('movie_id')
            if not name or not age or not gender or not movie_id:
                abort(422)
            actor.name = name
            actor.age = age
            actor.gender = gender
            actor.move_id = movie_id
            actor.update()
            return jsonify({
                'status': True,
                'message': 'Update actor successfully',
                'actor': actor.format()
            })
        except BaseException as e:
            print(e)
            abort(422)

    @app.route('/actors/<int:actor_id>/delete', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_actor(jwt, actor_id):
        actor = Actor.query.get(actor_id)
        if not actor:
            abort(404)
        try:
            actor.delete()
            return jsonify({
                'status': True,
                'message': 'Delete actor successfully',
                'actor_id': actor_id
            })
        except BaseException as e:
            print(e)
            abort(422)

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            'status': False,
            'error': 422,
            'message': 'Unprocessable'
        })

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'status': False,
            'error': 404,
            'message': 'Not found'
        })

    @app.errorhandler(AuthError)
    def auth_error(error):
        return jsonify({
            'status': False,
            'error': error.status_code,
            'message': error.error
        })
    return app


APP = create_app()

if __name__ == '__main__':
    # APP.run(host='0.0.0.0', port=8080, debug=True)
    APP.run()
