from operator import itemgetter

movies = [
    {
        "name" : "inception",
        "year" : 2010,
        "rating" : 8.7
    },
    {
        "name" : "inside out",
        "year" : 2015,
        "rating" : 8.1
    },
    {
        "name" : "con air",
        "year" : 1997,
        "rating" : 6.9
    }
]

def edit_list(name, year, rating, operation = "a"):
    name = name.lower()
    if operation == "a":
        movies.append({
            "name" : name,
            "year" : year,
            "rating" : rating
        })
    if operation == "c":
        try:
            movies[list(map(itemgetter('name'), movies)).index(name)] = {
                "name" : name,
                "year" : year,
                "rating" : rating
            }
        except ValueError:
            print("Filmen finnes ikke i listen")
    if operation == "r":
        try:
            movies.pop(list(map(itemgetter('name'), movies)).index(name))
        except ValueError:
            print("Filmen finnes ikke i listen")
