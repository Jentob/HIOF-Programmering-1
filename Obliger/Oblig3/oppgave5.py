import json

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

def add_movie(*movie):
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

def print_movies():
    for i in movies:
        print(f"{i['name'].title()} - {i['year']} has a rating of {i['rating']}")

def average_rating(movies):
    average = 0
    for i in movies:
        average += i["rating"]
    average /= len(movies)
    return average

def movies_year(movies, year):
    result = []
    for i in movies:
        if i["year"] == year:
            result.append(i)
    return result

def write_file(movies, file_name):
    file = open(file_name, "w")
    file.write(json.dumps(movies))

def print_from_file(file_name):
    file = open(file_name)
    file_content  = json.loads(file.read())
    for i in file_content:
        print(f"{i['name'].title()} - {i['year']} has a rating of {i['rating']}")

print(movies)
add_movie("ijof", 500)
add_movie("dfspofsp", 1233, 3.4)
add_movie("f3fw", 2, 8.1)
print(movies)

print_movies()

print(average_rating(movies))

print(movies_year(movies, 2010))

write_file(movies, "text.txt")
print_from_file("text.txt")
