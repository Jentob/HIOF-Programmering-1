print("hva er meningen med livet?")
while True:
    try:
        user_input = int(input())
        break
    except ValueError:
        print("Skriv inn et tall")
        continue

if user_input == 42:
    print("Det stemmer, meningen med liver er 42!")
elif (user_input >= 30) and (user_input <= 50):
    print("Nærme, men feil.")
else:
    print("FEIL!")
