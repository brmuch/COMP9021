# Prompts the user for two numbers, say available_digits and desired_sum, and
# outputs the number of ways of selecting digits from available_digits
# that sum up to desired_sum.


import sys
def get_sum(digits, current_sum, desired_sum):
    if len(str(digits)) == 1:
        if digits + current_sum == desired_sum or current_sum == desired_sum:
            return 1
        else:
            return 0
    else:
        result1 = get_sum(digits//10, current_sum, desired_sum)
        result2 = get_sum(digits//10, current_sum + digits % 10, desired_sum)
        return result1 + result2
# Insert your code here
if __name__ == "__main__":
    available_digits = int(input("Input a number that we will use as available digits: "))
    desired_sum = int(input("Input a number that represents the desired sum: "))
    value = get_sum(available_digits, 0, desired_sum)
    if value > 1:
        print(f"There are {value} solutions.")
    elif value == 1:
        print("There is a unique solution.")
    else:
        print("There is no solution.")


