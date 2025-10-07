movies = []

def add_movie(name: str):
    movies.append(name)

def delete_movie(name: str):
    movies.remove(name)

def show_movies():
    movies_list: str= ''
    for movie in movies:
        movies_list = movies_list + movie + '\n'
    return movies_list