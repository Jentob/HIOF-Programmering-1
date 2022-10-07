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

def add_movie(name, year, rating = 5.0):
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

print("\nPrinter ut listen")
print_movies()
add_movie("the Shawshank Redemption", 1994, 9.2)
add_movie("The Godfather", 1972, 9.2)
add_movie("The dark Knight", 2008, 9.0)
print("\nLegger til tre filmer")
print_movies()
add_movie("12 Angry Men", "1957")
print("\nLegger til film uten rating")
print_movies()
print("\nGjennonsnittsrating")
print(average_rating(movies))
print("\nPrinter ut filmer fra 2010")
print(movies_year(movies, 2010))

print("\nSkriver til en tekstfil og leser og printer den ut")
write_file(movies, "filmer.txt")
print_from_file("filmer.txt")
