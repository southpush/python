

# Score categories.
# Change the values as you see fit.
YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11


def score(dice, category):
    if category == YACHT:
        return 50 if len(set(dice)) == 1 else 0

    if ONES <= category <= SIXES:
        return category * dice.count(category)

    if category == FULL_HOUSE:
        return sum(dice) if len(set(dice)) == 2 and dice.count(dice[0]) in (2, 3) else 0

    if category == FOUR_OF_A_KIND:
        for i in dice:
            if dice.count(i) >= 4:
                return i * 4
        return 0

    if category == LITTLE_STRAIGHT:
        return 30 if sorted(dice) == [1, 2, 3, 4, 5] else 0

    if category == BIG_STRAIGHT:
        return 30 if sorted(dice) == [2, 3, 4, 5, 6] else 0

    if category == CHOICE:
        return sum(dice)

