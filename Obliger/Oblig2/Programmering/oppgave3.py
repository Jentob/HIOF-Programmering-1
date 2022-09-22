book_list = [
    "The Hobbit",
    "Farmer Giles of Ham",
    "The Fellowship of the Ring",
    "The Two Towers",
    "The Return of the King",
    "The Adventures of Tom Bombadil",
    "Tree and Leaf"
]

print(f"{book_list[0]}\n{book_list[1]}\n{book_list[len(book_list) - 1]}\n{book_list[len(book_list) - 2]}\n")

book_list.extend([
    "The Silmarillion",
    "Unfinished Tales"
])

for i in range(2, 5):
    book_list[i] = "The Lord of the Rings: " + book_list[i]

book_list.sort()

for i in book_list:
    print(i)
