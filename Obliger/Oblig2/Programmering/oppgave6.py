packing_list = []
add_no_argument = "Legg til argument. Eksempel: add bukser"
remove_no_argument = "Legg til argument. Eksempel: remove bukser"
welcome_message = """-----------------
PAKKELISTEPROGRAM
-----------------
Kommandoer:
    list / l - Skriver ut pakkelisten
    add / a - Legger til i listen. Eksempel: add bukser
    remove / r - Fjerner fra listen. Eksempel: remove bukser
    quit / q - Avslutter programmet"""
print(welcome_message)
while True:
    user_input = input().lower().split()
    if (user_input[0] == "quit" or user_input[0] == "q") and len(user_input) == 1:
        break

    if (user_input[0] == "list" or user_input[0] == "l") and len(user_input) == 1:
        if len(packing_list) == 0:
            print("Listen er tom")
            continue
        print("Liste:")
        for i in packing_list:
            print(f"\t{i}")
        continue

    if user_input[0] == "add" or user_input[0] == "a":
        if len(user_input) < 2:
            print(add_no_argument)
            continue
        del user_input[0]
        user_input = " ".join(user_input)
        if user_input in packing_list:
            print(f"{user_input.capitalize()} finnes allerede i listen")
        else:
            packing_list.append(user_input)
            print(f"La til {user_input} i listen")
        continue

    if user_input[0] == "remove" or user_input[0] == "r":
        if len(user_input) < 2:
            print(remove_no_argument)
            continue
        del user_input[0]
        user_input = " ".join(user_input)
        if user_input in packing_list:
            packing_list.remove(user_input)
            print(f"Fjernet {user_input} fra listen")
        else:
            print(f"Finner ikke {user_input} i listen")
        continue
