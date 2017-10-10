import webbrowser

class Movie():
    #declares the Movie class and necessary attributes for each film
    def __init__(self, movie_title, poster_image, trailer_youtube):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
    #define function for opening YouTube trailer link
        webbroswer.open(self.trailer_youtube_url)
