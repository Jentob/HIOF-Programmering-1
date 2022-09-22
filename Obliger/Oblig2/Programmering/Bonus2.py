import random

miss_chance = 0.1  # 10% sjanse for å bomme
bullseye_chance = 0.05  # 5% sjanse for å treffe bullseye
inner_chance = 0.3  # 30% sjanse for at et bullseye-treff treffer inner

start_message = "DART 3.0"
player_amount_msg = "Hvor mange skal spille?"
not_a_valid_number = "Skriv inn et tall større enn 1"

def throw():
    if random.random() <= miss_chance:
        return [0, 0]
    if random.random() <= bullseye_chance:
        if random.random() <= inner_chance:
            return [50, 0]
        else:
            return [25, 0]
    score = random.randrange(1, 20)
    multiply = random.randrange(1, 3)
    score *= multiply
    return [score, multiply]

print(start_message)
print(player_amount_msg)
while True:
    player_amount = input()
    try:
        player_amount = int(player_amount)
        if player_amount < 1:
            print(not_a_valid_number)
            continue
        player_scores = [301] * player_amount
        break
    except ValueError:
        print(not_a_valid_number)
        continue

class Winner(Exception):
    pass
class Unwinnable(Exception):
    pass
while True:
    try:
        for i in range(player_amount):
            score = throw()
            if player_scores[i] == 301 or player_scores[i] - score[0] < 1:
                if score[1] == 2 and player_scores[i] - score[0] >= 0:
                    player_scores[i] -= score[0]
                    print(f"Spiller {i + 1} fikk {score[0]} poeng. De må få {player_scores[i]} poeng til for å vinne.")
                else:
                    print(f"Spiller {i + 1} fikk 0 poeng. De må få {player_scores[i]} poeng til for å vinne.")

            else:
                player_scores[i] -= score[0]
                print(f"Spiller {i + 1} fikk {score[0]} poeng. De må få {player_scores[i]} poeng til for å vinne.")
            if player_scores[i] == 0:
                raise Winner
            if sum(player_scores) == player_amount:
                raise Unwinnable
    except Winner:
        print(f"Spiller {i + 1} vant!")
        print([player_scores])
        break

    except Unwinnable:
        print("Alle har ett(1) poeng så ingen vinner")
        print([player_scores])
        break
