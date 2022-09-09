import random

player_scores = []
score = 0

throws = 3
message = "Skriv inn antall spillere:"

print(message)
while True:
    try:
        player_amount = int(input())
        break
    except ValueError:
        print(message)
        continue
print()

for i in range(player_amount):
    for j in range(throws):
        score += random.randrange(0, 60)
        # print(score)
    player_scores.append(score)
    score = 0
    print(f"Spiller {i + 1} fikk {player_scores[i]} poeng.")

print()
print(f"Spiller {player_scores.index(max(player_scores)) + 1} vant!")
