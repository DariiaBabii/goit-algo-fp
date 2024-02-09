import random
from collections import defaultdict
import matplotlib.pyplot as plt

nums = 1_000_000

counts = defaultdict(int)

for _ in range(nums):
    dice = random.randint(1, 6)
    #counts[dice] += 1
    dice_two = random.randint(1, 6)
    counts[dice + dice_two] += 1

probabilities = {key: count / nums for key, count in counts.items()}
print("Dice | Probabilities")
print("-----|--------------")
for dice, prob in probabilities.items():
    print(f"{dice}    | {prob:2%}")

plt.bar(probabilities.keys(), probabilities.values())
plt.title('Ймовірності кожної суми')
plt.xlabel('Сума')
plt.ylabel('Імовірність')
plt.grid(True)

plt.show()
