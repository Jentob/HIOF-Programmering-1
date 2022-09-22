movies = [
    {
        "name" : "Inception",
        "year" : 2010,
        "rating" : 8.7
    },
    {
        "name" : "Inside Out",
        "year" : 2015,
        "rating" : 8.1
    },
    {
        "name" : "Con Air",
        "year" : 1997,
        "rating" : 6.9
    }
]

def edit_list(*movie, operation):
    if operation == "a":
        add(movie)
    if operation == "r":
        remove(movie)
    if
    name = movie[0]
    year = movie[1]
    if len(movie) < 3:
        rating = 5.0
    else:
        rating = movie[2]
    movies.append({
        "name" : name,
        "year" : year,
        "rating" : rating
    })
