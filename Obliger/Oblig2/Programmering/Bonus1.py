import random

miss_chance = 0.1  # 10% sjanse for å bomme
bullseye_chance = 0.05  # 5% sjanse for å treffe bullseye
inner_chance = 0.3  # 30% sjanse for at et bullseye-treff treffer inner

start_message = "DART 2.0"
player_amount_msg = "Hvor mange skal spille?"
dart_amount_msg = "Hvor mange darts skal kastes?"
round_amount_msg = "Hvor mange runder skal spilles?"
not_a_valid_number = "Skriv inn et tall større enn 1"

def throw():
    if random.random() <= miss_chance:
        return 0
    if random.random() <= bullseye_chance:
        if random.random() <= inner_chance:
            return 50
        else:
            return 25
    score = random.randrange(1, 20)
    score *= random.randrange(1, 3)
    return score


print(start_message)
print(player_amount_msg)
while True:
    player_amount = input()
    try:
        player_amount = int(player_amount)
        if player_amount < 1:
            print(not_a_valid_number)
            continue
        player_scores = [0] * player_amount
        break
    except ValueError:
        print(not_a_valid_number)
        continue
print(dart_amount_msg)
while True:
    dart_amount = input()
    try:
        dart_amount = int(dart_amount)
        if dart_amount < 1:
            print(not_a_valid_number)
            continue
        break
    except ValueError:
        print(not_a_valid_number)
        continue
print(round_amount_msg)
while True:
    round_amount = input()
    try:
        round_amount = int(round_amount)
        if round_amount < 1:
            print(not_a_valid_number)
            continue
        break
    except ValueError:
        print(not_a_valid_number)
        continue

for i in range(round_amount):
    for j in range(player_amount):
        for k in range(dart_amount):
            player_scores[j] += throw()
for i in range(player_amount):
    print(f"Spiller {i + 1} fikk {player_scores[i]} poeng")
if len(player_scores) > 1:
    print(f"Spiller {player_scores.index(max(player_scores)) + 1} vant!")
