"""
C = 3
For getting a card to the next room, I need 3 cards.
I can put one more card in the next room at the cost of 3 cards.

If there are 3 rooms, there are 4 doors.
I need to get to room 1 with 3 cards.


Let's say there are 4 rooms.
I need to get to room 2 with 3 cards.
I need to get to room 2 with 2 cards, and have one there.
I need to get to room 1 with 2 cards, and have one there.


Let's say there are 6 rooms. Answer is 123 cards.

I need to get to room 4 with 3 cards.
I need to get to room 4 with 2 cards, and have one there.
I need to get to room 3 with 2 cards, and have one there.
I need to get to room 2 with 2 cards, and have one there.
I need to get to room 1 with 2 cards, and have one there.

For taking a card to the next room, I need 3 cards in the previous one.

Una carta en room 4, tengo que llevar 3 a room 3.
4 en room 3. 12 en room 2. 13 en room 2.
39 en room 1. 40 en room 1.
120 de inicio. + 3 últimas: 123 final answer?

--------------------------------------

Rooms 6, cards 4
We need to get to room 3 with 4 cards.
We need to get to room 3 with 3 cards, and have one there.
We need to get to room 2 with 3 cards, and have one there.
We need to get to room 1 with 3 cards, and have one there.

Una carta en room 3, tengo que llevar 3 a room 2 (+1 de room 2) = 4 en room 2
Para llevar 4 a room 2, lo puedo hacer a partir de 8 desde room 1. (+1 de room 1) = 9 en room 1
Para llevar 9 a room 1, lo puedo hacer con 18 desde el origen.
NO. Para llevar 9, necesito llevar 8 + 1. Para llevar 8, necesito 16, para llevar 1, necesito 3.
16 + 3 = 19.

19 + 4 llaves que me cojo al principio = 23.
"""
def keys_required_on_lower_level(cards_top_level, max_cards_carry):
    # Two are needed to advance and get back from the room, so subtract them.
    cards_deposit_at_a_time = max_cards_carry - 2
    full_deposits = cards_top_level // cards_deposit_at_a_time
    full_deposits_total_cards = full_deposits * max_cards_carry

    spare_cards = cards_top_level % cards_deposit_at_a_time
    full_spare_cards = spare_cards + 2 if spare_cards != 0 else 0

    return full_deposits_total_cards + full_spare_cards

def keys_needed(max_cards_carry, rooms):
    """
    Parameters
    ----------
    max_cards_carry : int
        Number of cards you can carry at most at the same time.
    rooms : int
        Number of rooms you have to go through. Note that there will be a
        total of `rooms + 1` doors to go through.

    Returns
    -------
    int
        The total number of cards that must be used to go through all the
        doors.
    """
    if max_cards_carry == rooms:
        return rooms + 3
    if max_cards_carry >= rooms:
        return rooms + 1

    steps = rooms - max_cards_carry + 1
    res = 1
    for i in range(steps):
        res = keys_required_on_lower_level(res, max_cards_carry) + 1

    # Subtract one because in the last level, we don't need an extra one
    return res + max_cards_carry - 1

assert keys_required_on_lower_level(8, 4) == 16
assert keys_required_on_lower_level(9, 4) == 19
assert keys_required_on_lower_level(1, 3) == 3
assert keys_required_on_lower_level(4, 3) == 12
assert keys_required_on_lower_level(13, 3) == 39
assert keys_required_on_lower_level(1, 4) == 3

assert keys_needed(3, 3) == 6
assert keys_needed(3, 6) == 123
assert keys_needed(4, 6) == 23
assert sum([keys_needed(i, 10) for i in range(3, 11)]) == 10382

print(sum([keys_needed(i, 30) for i in range(3, 41)])) # Answer is 34315549139516