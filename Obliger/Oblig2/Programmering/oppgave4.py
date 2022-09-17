import re

oppgave3_list = [
    "Farmer Giles of Ham",
    "The Adventures of Tom Bombadil",
    "The Hobbit",
    "The Lord of the Rings: The Fellowship of the Ring",
    "The Lord of the Rings: The Return of the King",
    "The Lord of the Rings: The Two Towers",
    "The Silmarillion",
    "Tree and Leaf",
    "Unfinished Tales"
]

new_list = []

for i in oppgave3_list:
    if re.search("^The Lord of the Rings", i):
        new_list.append(i)

for i in new_list:
    print(i)
