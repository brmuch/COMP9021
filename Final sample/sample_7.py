'''
Tries and find a word in a text file that represents a grid of words, all of the same length.
There is only one word per line in the file.
The letters that make up a word can possibly be separated by an arbitrary number of spaces,
and there can also be spaces at the beginning or at the end of a word,
and there can be lines consisting of nothing but spaces anywhere in the file.
Assume that the file stores data as expected.

A word can be read horizontally from left to right,
or vertically from top to bottom,
or diagonally from top left to bottom right
(this is more limited than the lab exercise).
The locations are represented as a pair (line number, column number),
starting the numbering with 1 (not 0).
'''
import re

def find_word(filename, word):
    '''
    >>> find_word('word_search_1.txt', 'PLATINUM')
    PLATINUM was found horizontally (left to right) at position (10, 4)
    >>> find_word('word_search_1.txt', 'MANGANESE')
    MANGANESE was found horizontally (left to right) at position (11, 4)
    >>> find_word('word_search_1.txt', 'LITHIUM')
    LITHIUM was found vertically (top to bottom) at position (2, 14)
    >>> find_word('word_search_1.txt', 'SILVER')
    SILVER was found vertically (top to bottom) at position (2, 13)
    >>> find_word('word_search_1.txt', 'SODIUM')
    SODIUM was not found
    >>> find_word('word_search_1.txt', 'TITANIUM')
    TITANIUM was not found
    >>> find_word('word_search_2.txt', 'PAPAYA')
    PAPAYA was found diagonally (top left to bottom right) at position (1, 9)
    >>> find_word('word_search_2.txt', 'RASPBERRY')
    RASPBERRY was found vertically (top to bottom) at position (5, 14)
    >>> find_word('word_search_2.txt', 'BLUEBERRY')
    BLUEBERRY was found horizontally (left to right) at position (13, 5)
    >>> find_word('word_search_2.txt', 'LEMON')
    LEMON was not found
    '''
    with open(filename) as file:
        grid = None
        # Insert your code here
        grid = list()
        for line in file.readlines():
            line = re.sub(r"\s",'', line)
            grid.append(line)
        grid = [x for x in grid if x != '']

        # A one liner that sets grid to the appropriate value is enough.
        location = find_word_horizontally(grid, word)
        found = False
        if location:
            found = True
            print(word, 'was found horizontally (left to right) at position', location)
        location = find_word_vertically(grid, word)
        if location:
            found = True
            print(word, 'was found vertically (top to bottom) at position', location)
        location = find_word_diagonally(grid, word)
        if location:
            found = True
            print(word, 'was found diagonally (top left to bottom right) at position', location)
        if not found:
            print(word, 'was not found')
    
    
def find_word_horizontally(grid, word):
    # Replace pass above with your code
    for i in range(0, len(grid)):
        if word in grid[i]:
            return (i + 1, grid[i].find(word) + 1)

def find_word_vertically(grid, word):
    # Replace pass above with your code
    grid1 = list()
    for i in range(0, len(grid[0])):
        temp = ''
        for j in range(0, len(grid)):
            temp += grid[j][i]
        grid1.append(temp)

    for i in range(0, len(grid1)):
        if word in grid1[i]:
            return (grid1[i].find(word) + 1, i + 1)

def find_word_diagonally(grid, word):
    # Replace pass above with your code
    grid2 = list()
    for i in range(0, len(grid[0])):
        num = i
        temp = ''
        line = 0
        while num < len(grid[0]):
            temp += grid[line][num]
            line += 1
            num += 1
        grid2.append(temp)
    for j in range(1, len(grid)):
        num = j
        temp = ''
        row = 0
        while num < len(grid):
            temp += grid[num][row]
            row += 1
            num += 1
        grid2.append(temp)

    for i in range(0, len(grid2)):
        if word in grid2[i]:
            return (grid2[i].find(word) + 1, (i + 1) % len(grid[0]))

if __name__ == '__main__':
    import doctest
    doctest.testmod()   
