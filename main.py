from movies.movie import add_movie, movies
from movies.movie import delete_movie
from movies.movie import show_movies


def main():
    add_movie('The Matrix')
    add_movie('The Lord of the Rings')
    add_movie('Leon')
    add_movie('The Hobbit')
    add_movie('Smaug')
    add_movie('The War of the Worlds')
    show_movies()

    print(movies)

if __name__ == '__main__':
    main()