from functools import *

list_input = open('input.txt', 'r').read().split('\n')

pawn_1 = int(list_input[0].split(": ")[1])
pawn_2 = int(list_input[1].split(": ")[1])

d = [1, 2, 3]
possible_dice_rolls = [a + b + c for a in d for b in d for c in d]

@cache
def rec(player_1_score, player_2_score, pawn_1, pawn_2) -> list[int]:
    result = [0, 0]
    for dice_roll in possible_dice_rolls:
        new_pawn = (pawn_1 + dice_roll - 1) % 10 + 1
        new_score = player_1_score + new_pawn
        if new_score >= 21:
            result[0] += 1
            continue
        rec_result = rec(player_2_score, new_score, pawn_2, new_pawn)
        result[0] += rec_result[1]
        result[1] += rec_result[0]
    return result

print(max(rec(0, 0, pawn_1, pawn_2)))
