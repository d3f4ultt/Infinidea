import itertools
import random
import math

with open('input.txt', 'r') as f:
    entities = [line.strip() for line in f]

num_combinations = math.comb(len(entities), 2) + math.comb(len(entities), 3)
print(f"Number of possible combinations: {num_combinations}")

combinations = list(itertools.combinations(entities, 2)) + list(itertools.combinations(entities, 3))

random.shuffle(combinations)

# convert combinations from tuples to strings
combinations = [' '.join(comb) for comb in combinations]

output_counter = 1
comb_counter = 0

for comb in combinations:
    if comb_counter % 400 == 0 and comb_counter > 0:
        answer = input("Do you want to continue? (yes/no) ")
        if answer.lower() != "yes":
            break
        output_counter += 1

    with open(f'output{output_counter}.txt', 'a') as f:
        f.write(f"{comb}\n")
        print(comb)
    
    comb_counter += 1
