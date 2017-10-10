def read_text():
    quotes = open("C:/Users/ThunderBear/Documents/Udacity/full_stack_web/lesson8_ProfanityEditor/movie_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    
read_text()
