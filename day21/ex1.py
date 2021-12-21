list_input = open('input.txt', 'r').read().split('\n')

pawn_1 = int(list_input[0].split(": ")[1])
pawn_2 = int(list_input[1].split(": ")[1])

dice = 0
player_1_score = 0
player_2_score = 0
die_rolled = 0
while player_1_score < 1000 and player_2_score < 1000:
    die_rolled += 3
    dice_value = (dice * 3 + 6 - 1) % 100 + 1
    dice += 3
    pawn_1 = (pawn_1 + dice_value - 1) % 10 + 1
    player_1_score += pawn_1
    if (player_1_score >= 1000):
        break
    die_rolled += 3
    dice_value = (dice * 3 + 6 - 1) % 100 + 1
    dice += 3
    pawn_2 = (pawn_2 + dice_value - 1) % 10 + 1
    player_2_score += pawn_2

print(min(player_1_score, player_2_score) * die_rolled)
