class Movie:
    def __init__(self, title, year, score):
        self.title = title
        self.year = year
        self.score = score

    def __str__(self):
        return f"{self.title.title()} was released in {self.year} and currently has a score of {self.score}"


inception = Movie("inception", 2010, 8.8)
the_martian = Movie("the martian", 2015, 8.0)
joker = Movie("Joker", 2019, 8.4)

print(f"{inception}\n{the_martian}\n{joker}\n")
