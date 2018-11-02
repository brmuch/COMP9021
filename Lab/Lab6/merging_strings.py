# Say that two strings s_1 and s_2 can be merged into a third
# string s_3 if s_3 is obtained from s_1 by inserting
# arbitrarily in s_1 the characters in s_2, respecting their
# order. For instance, the two strings ab and cd can be merged
# into abcd, or cabd, or cdab, or acbd, or acdb..., but not into
# adbc nor into cbda.
#
# Prompts the user for 3 strings and displays the output as follows:
# - If no string can be obtained from the other two by merging,
# then the program outputs that there is no solution.
# - Otherwise, the program outputs which of the strings can be obtained
# from the other two by merging.


# Insert your code here
def judge(current, first, second, third):
    if len(first) == 0:
        return True if current + second == third or current == third else False
    elif len(second) == 0:
        return True if current + first == third or current == third else False
    elif current == third:
        return True
    else:
        result1 = judge(current + first[0], first[1::], second, third)
        result2 = judge(current + second[0], first, second[1::], third)
        result3 = judge(current + first[0] + second[0], first[1::], second[1::], third)
        result4 = judge(current + second[0] + first[0], first[1::], second[1::], third)
        return result1 or result2 or result3 or result4
if __name__ == "__main__":
    first = input("Please input the first string: ")
    second = input("Please input the second string: ")
    third = input("Please input the third string: ")
    result1 = judge('', first, second, third)
    result2 = judge('', first, third, second)
    result3 = judge('', second, third, first)
    if result3 and len(first) == max(len(first), len(second), len(third)):
        print("The first string can be obtained by merging the other two.")
    elif result2 and len(second) == max(len(first), len(second), len(third)):
        print("The second string can be obtained by merging the other two.")
    elif result1 and len(third) == max(len(first), len(second), len(third)):
        print("The third string can be obtained by merging the other two.")
    else:
        print("No solution")
