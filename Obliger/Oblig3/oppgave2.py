import random

def generate_number():
    number = random.randrange(0, 100)
    print("**" + "*" * len(str(number)))
    print(f"*{number}*")
    print("**" + "*" * len(str(number)))
    print()

generate_number()
generate_number()
generate_number()
generate_number()
