import media
import fresh_tomatoes


def main():
    """ main function for creating the website """

    # create the instances of movies
    la_la_land = media.Movie("LA LA LAND",
                                "A story of chasing dreams",
                                "https://upload.wikimedia.org/wikipedia/en/a/ab/La_La_Land_%28film%29.png",  # NOQA
                                "https://www.youtube.com/watch?v=0pdqf4P9MB8")  # NOQA

    transformers = media.Movie("TRANSFORMERS",
                                "Robots from outerspace",
                                "https://upload.wikimedia.org/wikipedia/en/6/66/Transformers07.jpg",  # NOQA
                                "https://www.youtube.com/watch?v=yCOvcyfRPRk")  # NOQA

    about_time = media.Movie("about Time",
                                "A man with special ability to time travel",
                                "https://upload.wikimedia.org/wikipedia/en/8/88/About_Time_Poster.jpg",  # NOQA
                                "https://www.youtube.com/watch?v=r9uVnxEqMkE")  # NOQA

    devil_wears_prada = media.Movie("THE DEVIL WEARS PRADA",
                                        "A story about the fashion industry",
                                        "https://upload.wikimedia.org/wikipedia/en/e/e7/The_Devil_Wears_Prada_main_onesheet.jpg",  # NOQA
                                        "https://www.youtube.com/watch?v=XTDSwAxlNhc")  # NOQA

    frozen = media.Movie("FROZEN",
                            "Anna and her sister Elsa",
                            "https://upload.wikimedia.org/wikipedia/en/0/05/Frozen_%282013_film%29_poster.jpg",  # NOQA
                            "https://www.youtube.com/watch?v=R-cdIvgBCWY")  # NOQA

    if_only = media.Movie("If Only",
                            "The romance of a businessman and a musician",
                            "https://upload.wikimedia.org/wikipedia/en/9/9b/If_Only_movie_poster.jpg",  # NOQA
                            "https://www.youtube.com/watch?v=3z5XDNHmBco")  # NOQA

    music_and_lyrics = media.Movie("music and lyrics",
                                    "A pop music idol and an aspiring writer",
                                    "https://upload.wikimedia.org/wikipedia/en/d/d3/Music_and_lyrics.jpg",  # NOQA
                                    "https://www.youtube.com/watch?v=4C6sSZlVKZE")  # NOQA

    # create a list contains all the movies
    movies = [
        la_la_land, transformers, about_time,
        devil_wears_prada, frozen, if_only,
        music_and_lyrics
    ]

    # pass the list the fresh_tomatoes to create the website
    fresh_tomatoes.open_movies_page(movies)

if __name__ == '__main__':
    main()
