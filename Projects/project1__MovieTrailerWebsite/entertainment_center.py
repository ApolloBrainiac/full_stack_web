import fresh_tomatoes
# Connects movie list to program that will generate trailer site
import media
# Connects movie list to library with Movie class

blade_runner = media.Movie("Blade Runner",
                           "https://upload.wikimedia.org/wikipedia/en/5/53/Blade_Runner_poster.jpg",
                           "https://www.youtube.com/watch?v=eogpIG53Cis")

save_the_green_planet = media.Movie("Save the Green Planet!",
                                    "https://upload.wikimedia.org/wikipedia/en/6/67/Save_the_Green_Planet_Poster.jpg",
                                    "https://www.youtube.com/watch?v=_H-hPpPMu4A")

city_of_lost = media.Movie("City of Lost Children",
                           "https://upload.wikimedia.org/wikipedia/en/4/40/City_of_lost_children_french_movie_poster.jpg",
                           "https://www.youtube.com/watch?v=CNYG9cXTSds")

tekkonkinkreet = media.Movie("Tekkonkinkreet",
                             "https://images-na.ssl-images-amazon.com/images/M/MV5BMTkzMDMzMzQwOV5BMl5BanBnXkFtZTgwNDAxNzkwMzE@._V1_UX182_CR0,0,182,268_AL_.jpg",
                             "https://www.youtube.com/watch?v=W2ku5toXWFc")

in_the_loop = media.Movie("In the Loop",
                          "http://www.gstatic.com/tv/thumb/movieposters/196286/p196286_p_v8_aa.jpg",
                          "https://www.youtube.com/watch?v=dQrqMkCuHqA")

eternal_sunshine = media.Movie("Eternal Sunshin of the Spotless Mind",
                               "https://upload.wikimedia.org/wikipedia/en/6/62/Eternal_sunshine_of_the_spotless_mind_ver3.jpg",
                               "https://www.youtube.com/watch?v=0zFywiAh7N0")
                               




movies = [blade_runner, 
          save_the_green_planet, 
          city_of_lost, tekkonkinkreet, 
          in_the_loop, 
          eternal_sunshine]
#saves the current list of films into a library so fresh_tomatoes can populate the trailer site


fresh_tomatoes.open_movies_page(movies)
#accesses fresh_tomatoes to produce trailer site

