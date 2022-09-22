def print_list(input_list):
    if isinstance(input_list, list) is False:
        print("Ikke en liste!")
        return
    for i in input_list:
        print(i.capitalize())


print_list(["Pizza", "Taco", "Sushi"])
