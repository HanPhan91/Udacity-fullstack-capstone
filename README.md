# App Capstone Backend

    This is final project for Udacity's FullStack Web Developer Nanodegree. Web app can be accessed at URL: https://udacity-fullstack-capstone-1.onrender.com/

## Installation instructions

    Run `pip install -r requirements.txt` to install project dependencies
    Change infomation in `.env`
    Type `python app.py` to run project

## Roles

    Casting Assistant
        GET /actors and /movies
    Casting Director
        GET /actors and /movies
        ADD /actors and DELETE /actors
        PATCH /actors and /movies
    Executive Producer
        GET /actors and /movies
        ADD /actors and DELETE /actors
        PATCH /actors and /movies
        ADD /movies and DELETE /movies

## JWT Token for each role

    Casting Assistant:
        eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IktfRU52NFljNnVucUQwaHJwT1dBUyJ9.eyJpc3MiOiJodHRwczovL2hhbnBnMy51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjY5OWNlMGQ4MzNiNjMwNjZiNjhkMzE4IiwiYXVkIjoiYXBpIiwiaWF0IjoxNzIxMzY4ODE3LCJleHAiOjE3MjE0NDA4MTcsInNjb3BlIjoiIiwiYXpwIjoiSm5yQ2JqeTBtbm5qNUZhVFJGcno5dzVXQW11c212NmQiLCJwZXJtaXNzaW9ucyI6WyJ2aWV3OmFjdG9ycyIsInZpZXc6bW92aWVzIl19.S4XcWg9Q4PI-mcEzBD7WPMdskmxrJxqrHwUTQnsHv7XwqdJ8V27Er6f1XmGJu3cN05uqwZ2A9JhWHrrt8QtKe7fDNVRYGbGwS3TloR4PtYVQQWqoOQ6KqIxBJfignG5HVCNBi7w2kwshUxtEyGl2CuW2eGYi0gDmsRhfC8zTtkxfiNAu0fsPw--nEQuzMFGXgJAigHpchJoFDv2uNirkY26ACEwIUJKIJ98x4ZKyAnEFgzaQpbaZ9pkhNrHnaRU1AnQZqk9ZOPcPoQizalcsBP46NvFUvA3ouXrsDLsjxeQq3SBjgEcRLOOFfU6KVJcsAzhd1ZbIK5W4HQcCp5w_WQ

    Casting Director:
        eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IktfRU52NFljNnVucUQwaHJwT1dBUyJ9.eyJpc3MiOiJodHRwczovL2hhbnBnMy51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjY5OWNlZGMxMzZlMWFiZDk0ZGFlYmU3IiwiYXVkIjoiYXBpIiwiaWF0IjoxNzIxMzY4ODU3LCJleHAiOjE3MjE0NDA4NTcsInNjb3BlIjoiIiwiYXpwIjoiSm5yQ2JqeTBtbm5qNUZhVFJGcno5dzVXQW11c212NmQiLCJwZXJtaXNzaW9ucyI6WyJhZGQ6YWN0b3JzIiwiZGVsZXRlOmFjdG9ycyIsInVwZGF0ZTphY3RvcnMiLCJ1cGRhdGU6bW92aWVzIiwidmlldzphY3RvcnMiLCJ2aWV3Om1vdmllcyJdfQ.UsohhsEjwuVJDbJ_kx1KQqyBBSngPSOQ6OFH6dZeWwLQXfNjGlB0d7Je76TOM6FVCisFK57p8F3amCIKwqthZHPRovHZiB-Z742LYZ-HJuNaKnLmd91IZdH7Rxgtiq6bQFHGwW7GP4u2U6Vkcv2_sWOSYfChU3tWUT1r62WmXXhzVGpQduBIg6EZitd_ryWIcQam7fkW9z7gKJLv7JU0OE6P4iZOogjTAprKB6bfcvcT74lozyuLi_j6M1pvrivL14wchtOH-9d8FwDqj4LPZw_dZeAwFhKGvE6rYkhjOk1Ccq5e4JVOQ4-ddBJBDM0nJPIc6EYgCsLRnsJuSu8bxg

    Executive Producer:
        eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IktfRU52NFljNnVucUQwaHJwT1dBUyJ9.eyJpc3MiOiJodHRwczovL2hhbnBnMy51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjY5OWNmMDUxMzZlMWFiZDk0ZGFlYzIwIiwiYXVkIjoiYXBpIiwiaWF0IjoxNzIxMzY4ODg3LCJleHAiOjE3MjE0NDA4ODcsInNjb3BlIjoiIiwiYXpwIjoiSm5yQ2JqeTBtbm5qNUZhVFJGcno5dzVXQW11c212NmQiLCJwZXJtaXNzaW9ucyI6WyJhZGQ6YWN0b3JzIiwiYWRkOm1vdmllcyIsImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwidXBkYXRlOmFjdG9ycyIsInVwZGF0ZTptb3ZpZXMiLCJ2aWV3OmFjdG9ycyIsInZpZXc6bW92aWVzIl19.NFn-7h30_FS4bZgZxC2DfLh_vg9X1F9YfDa9LbLaYLuDRJn5Xa7li4ci2oUzlujw_f3jlutv4pCFQiIwJTxyb2aW_n6OiG5G9xlYNlVNsbLjXG6KwMQKwaqk6Ku46skW3LuNrObOnSe4Skr_fvhP9dQfMITwFC2eZHVlKxlrhaWF3iorwlxYbPDoEtELHz4NiuykLOQpKBnSxVfpIU5RR8AYjtjLALxlwknUal3FE_F9Cbe8yG3iKZJGVd5u6hEZ8FJ6_XcvWDbUvA5ktwogwO7SfYeWLXS6WGBfswkS7xsEzsEGrvQs949PD3C7z5CVtkozs-l7DwAF6VwuuF3Tig

## API Endpoints

    ### GET Enpoints
        #### GET /movies : Displays all movies.
        Sample response:
            {
                "message": "Get movies successfully",
                "movies": [
                    {
                    "id": 1,
                    "release_year": 2024,
                    "title": "update movie"
                    }
                ],
                "status": true
            }

        #### GET /actors: Displays all actors.
        Sample response:
            {
                "actors": [
                    {
                        "age": 30,
                        "gender": "male",
                        "id": 4,
                        "movie_id": 1,
                        "name": "actor name"
                    },
                ],
                "message": "Get actors successfully",
                "status": true
            }

    ### POST Enpoints
        #### POST /movies/add: Creates a new movie
        Sample response:
            {
                "message": "Add movie successfully",
                "movie": {
                    "id": 3,
                    "release_year": 2023,
                    "title": "add movie"
                },
                "status": true
            }

        #### POST /actors/add: Creates a new actor
        Sample response:
            {
                "actor": {
                    "age": 30,
                    "gender": "male",
                    "id": 5,
                    "movie_id": 1,
                    "name": "actor name"
                },
                "message": "Add actor successfully",
                "status": true
            }

    ### PATCH Enpoints
        #### PATCH /movies/<movie_id>/update : Updates movie information given a movie_id and newly updated attribute info.
        Sample response:
            {
                "message": "Update movie successfully",
                "movie": {
                    "id": 1,
                    "release_year": 2024,
                    "title": "update movie"
                },
                "status": true
            }

        #### PATCH /actors/<actor_id>/update : Updates actor information given a actor_id and newly updated attribute info.
        Sample response:
            {
                "actor": {
                    "age": 21,
                    "gender": "female",
                    "id": 3,
                    "movie_id": 1,
                    "name": "update actor"
                },
                "message": "Update actor successfully",
                "status": true
            }

    ### DELETE Enpoints
        #### DELETE /movies/<movie_id>/delete : Delete a movie entry from the database given the inputted movie_id.
        Sample response:
            {
                "actor_id": 3,
                "message": "Delete actor successfully",
                "status": true
            }

        #### DELETE /actors/<actor_id>/delete : Delete an actor / actress entry from the database given the inputted actor_id.
        Sample response:
            {
                "message": "Delete movie successfully",
                "movie_id": 3,
                "status": true
            }
