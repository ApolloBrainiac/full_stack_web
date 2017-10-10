import webbrowser

class Movie():
    #declares the Movie class and necessary attributes for each film
    def __init__(self, movie_title, poster_image_url, trailer_youtube_id):
        self.movie_title = movie_title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_id = trailer_youtube_id

    def show_trailer(self):
    #define function for opening YouTube trailer link
        webbroswer.open(self.trailer_youtube_id)


