from collections import defaultdict


def letter_count(word):
    '''
    Given a word, returns a dict where each entry is:
        (letter: letter_count)
    '''
    res = defaultdict(int)

    for l in word:
        res[l] += 1

    count = sorted(res.items(), key=lambda x: x[0])

    return tuple(count)



with open('p098_words.txt', 'r') as f:
    content = f.readlines()

words = []

for line in content:
    no_quotes = line.replace('"', '')
    words_raw = no_quotes.split(',')

    for w in words_raw:
        words.append(w)

print(len(words))

word_groups = defaultdict(lambda: [])
for w in words:
    word_groups[letter_count(w)].append(w)

print(len(word_groups))

# print(word_groups.keys())
valid_pairs = list(filter(lambda x: len(x[1]) > 1, word_groups.items()))
print(valid_pairs)
for k, v in word_groups.items():
    if len(v) != 1:
        print(v)
"""
Now, we need to check for the condition that the squares do indeed match.
For this, we can use the fact that we know the letters that are there.

Generate all possible squares of 4 digits. See which ones match, and somehow
apply something to see if the order of the letters is in the same order than
in the other word(s).
"""

"""
Functions I need:
- Function to check if a word may map to a square.
- Function to check if a word matches another square, given a mapping.
"""

def word_maps_square(word, number):
    """
    Function that checks whether a word maps to a number.
    If it does, returns the mapping to apply. If not, returns None.
    """
    n_str = str(number)

    mapping = defaultdict(str)

    if len(word) != len(n_str):
        return None

    for i in range(len(word)):
        letter = word[i]
        value = n_str[i]
        mapping[letter] = value

    # Check that the mapping is correct
    word_2 = word
    for k, v in mapping.items():
        word_2 = word_2.replace(k, v)

    number_obtained = int(word_2)

    # Check that each letter maps to a different number
    if len(set(word)) != len(set(mapping.values())):
        return None

    # Mapping correct
    if number_obtained == number:
        return mapping

    return None

assert word_maps_square('CARE', 1296) is not None
assert word_maps_square('AABB', 1296) is None

def mapped_word_is_square(word, mapping):
    w = word
    for k, v in mapping.items():
        w = w.replace(k, v)

    number = int(w)
    sqrt = int(number**0.5)
    return number == sqrt**2

assert mapped_word_is_square('RACE', {'R': '9', 'A': '2', 'C': '1', 'E': '6'})
assert not mapped_word_is_square('AB', {'A': '1', 'B': '0'})

"""
What is missing? For each pair of words: Generate all possible squares of that
length. For the first word: Find all possible matchings, and check against the
other. If its a match, store the highest.
"""
from math import ceil
from math import floor


def generate_all_squares(number_of_digits):
    """
    Returns a list containing all the squares with a specific number of
    digits.
    """
    lower = 10**(number_of_digits - 1)
    upper = 10**number_of_digits - 1

    lb = ceil(lower**0.5)
    ub = floor(upper**0.5)

    squares = []
    for i in range(lb, ub+1):
        squares.append(i**2)

    return squares

assert generate_all_squares(2) == [16, 25, 36, 49, 64, 81]

candidates = []

word_groups['123a'] = ['POST', 'SPOT']
word_groups['123b'] = ['POST', 'STOP']
word_groups['123c'] = ['STOP', 'SPOT']

for k, v in word_groups.items():
    # There is only one group with 3. We will assume solution is not there
    # If solution were not correct, we would have to take that case separately
    if len(v) != 2:
        continue

    w1 = v[0]
    w2 = v[1]

    l = len(w1)
    squares = generate_all_squares(l)

    for sq in squares:
        mapping = word_maps_square(w1, sq)
        if mapping is not None:
            if mapped_word_is_square(w2, mapping):
                candidates.append((w1, w2, mapping))

#candidates = list(filter(lambda x: len(set(x[1])) == len(set(x[2].values())), candidates))

print()
print(len(candidates))

FINAL_SOLUTIONS = []

# For each candidate, now we calculate the highest square
for w1, w2, mapping in candidates:
    w1_number = w1
    for k, v in mapping.items():
        w1_number = w1_number.replace(k, v)
    w1_number = int(w1_number)

    w2_number = w2
    for k, v in mapping.items():
        w2_number = w2_number.replace(k, v)
    w2_number = int(w2_number)

    FINAL_SOLUTIONS.append(w1_number)
    FINAL_SOLUTIONS.append(w2_number)

print(sorted(list(set(FINAL_SOLUTIONS))))
# Solution is 18769. Why not the first ones? Something to do with trailing
# zeroes?
