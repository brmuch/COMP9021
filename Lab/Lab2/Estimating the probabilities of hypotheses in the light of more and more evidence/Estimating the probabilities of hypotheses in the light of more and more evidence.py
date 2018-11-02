'''
Simulates the cast of an unknown die, chosen from a set of 5 dice with 4, 6, 8, 12, and 20 sides.

To start with, every die has a probability of 0.2 to be the chosen die.
At every cast, the probability of each die is updated using Bayes' rule.
The probabilities are displayed for at most 6 casts.
If more than 6 casts have been requested, the final probabilities obtained
for the chosen number of casts are eventually displayed.
'''


from random import choice, seed
import sys


dice = 4, 6, 8, 12, 20
chosen_dice = choice(dice)

while True:
    try:
        for_seed = int(input('Enter the seed: '))
        seed(for_seed)
        break
    except ValueError:
        pass

# Insert your code here
# Use choice() again when casting the die.
probability = [0.2] * 5
dice = choice(dice)
desired_number = int(
    input("Enter the desired number of times a randomly chosen die will be cast: "))
print(f"\nThis is a secret, but the chosen die is the one with {dice} faces")

for _ in range(0, desired_number):
    outcome = choice([x for x in range(1, dice + 1)])
    if(_ < 5):
        print(f"\nCasting the chosen die... Outcome: {outcome}")
        print("The updated dice probabilities are:")
    elif(_ == desired_number - 1):
        print("\nThe final probabilities are:")

    A1_B_A1 = (probability[0]) * (1 / 4)
    A2_B_A2 = (probability[1]) * (1 / 6)
    A3_B_A3 = (probability[2]) * (1 / 8)
    A4_B_A4 = (probability[3]) * (1 / 12)
    A5_B_A5 = (probability[4]) * (1 / 20)

    if(outcome <= 4):
        denominator = A1_B_A1 + A2_B_A2 + A3_B_A3 + A4_B_A4 + A5_B_A5
    elif(outcome <= 6):
        denominator = A2_B_A2 + A3_B_A3 + A4_B_A4 + A5_B_A5
        A1_B_A1 = 0
    elif(outcome <= 8):
        denominator = A3_B_A3 + A4_B_A4 + A5_B_A5
        A1_B_A1 = 0
        A2_B_A2 = 0
    elif(outcome <= 12):
        denominator = A4_B_A4 + A5_B_A5
        A1_B_A1 = 0
        A2_B_A2 = 0
        A3_B_A3 = 0
    else:
        denominator = A5_B_A5
        A1_B_A1 = 0
        A2_B_A2 = 0
        A3_B_A3 = 0
        A4_B_A4 = 0

    if(_ < 5 or desired_number - 1 == _):
        print(f"     4: {(100 * A1_B_A1 / denominator):.2f}%")
        print(f"     6: {(100 * A2_B_A2 / denominator):.2f}%")
        print(f"     8: {(100 * A3_B_A3 / denominator):.2f}%")
        print(f"    12: {(100 * A4_B_A4 / denominator):.2f}%")
        print(f"    20: {(100 * A5_B_A5 / denominator):.2f}%")
    #in ed system, \t is different with space

    probability[0] = (100 * A1_B_A1 / denominator)
    probability[1] = (100 * A2_B_A2 / denominator)
    probability[2] = (100 * A3_B_A3 / denominator)
    probability[3] = (100 * A4_B_A4 / denominator)
    probability[4] = (100 * A5_B_A5 / denominator)
