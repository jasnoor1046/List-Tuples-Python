# program to generate the combinations of the elements in a tuple.

import itertools

# this will allow us to generate combinations of different lengths.


def generate_combinations(tup):
    all_combinations = []
    for r in range(1, len(tup) + 1):

        # itertools.combinations is useful for generating all possible combinations of a specified length
        # from an input iterable.
        combinations_r = tuple(itertools.combinations(tup, r))
        all_combinations.extend(combinations_r)
    return all_combinations


user_input = input("Enter the elements of the tuple: ")
user_tuple = tuple(map(int, user_input.split(",")))

combinations = generate_combinations(user_tuple)

print("All combinations of tuple elements: ")

for combo in combinations:
    print(combo)
