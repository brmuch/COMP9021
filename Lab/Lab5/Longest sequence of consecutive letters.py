from copy import *
def Long_consecutive_letters(words):
    code = [ord(words[i]) for i in range(0, len(words))]

    result = []
    for i in range(0, len(code)):
        current = code[i]
        item = [current]
        temp = deepcopy(code[i+1:])

        while len(temp) > 0:
            m = temp.pop(0)
            if m == current + 1:
                current = m
                item.append(m)
        if len(item) > len(result):
            result = item

    result = [chr(x) for x in result]
    str = ''
    for i in result:
        str += i
    return str

if __name__  == "__main__":
    input = input("Please input a string of lowercase letters: ")
    length = 0
    max_length = 0
    consecutive_start_position = 0

    # Delete the same consecutive letters in the sequence
    string = ''
    for i in input:
        if (string != '' and i != string[-1]) or string == '':
            string += i

    consecutive_letters = Long_consecutive_letters(string)
    print(f"The solution is: {consecutive_letters}")
