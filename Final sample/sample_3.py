'''
Given a word w, a good subsequence of w is defined as a word w' such that
- all letters in w' are different;
- w' is obtained from w by deleting some letters in w.
Returns the list of all good subsequences, without duplicates, in lexicographic order
(recall that the sorted() function sorts strings in lexicographic order).
The number of good sequences grows exponentially in the number of distinct letters in w,
so the function will be tested only for cases where the latter is not too large.
'''

from itertools import combinations

def is_not_two_equal(list):
    for i in range(0, len(list) - 1):
        for j in range(i + 1, len(list)):
            if list[i] == list[j]:
                return False
    return True

def good_subsequences(word):
    '''
    >>> good_subsequences('')
    ['']
    >>> good_subsequences('aaa')
    ['', 'a']
    >>> good_subsequences('aaabbb')
    ['', 'a', 'ab', 'b']
    >>> good_subsequences('aaabbc')
    ['', 'a', 'ab', 'abc', 'ac', 'b', 'bc', 'c']
    >>> good_subsequences('aaabbaaa')
    ['', 'a', 'ab', 'b', 'ba']
    >>> good_subsequences('abbbcaaabccc')
    ['', 'a', 'ab', 'abc', 'ac', 'acb', 'b', 'ba', 'bac',\
 'bc', 'bca', 'c', 'ca', 'cab', 'cb']
    >>> good_subsequences('abbbcaaabcccaaa')
    ['', 'a', 'ab', 'abc', 'ac', 'acb', 'b', 'ba', 'bac',\
 'bc', 'bca', 'c', 'ca', 'cab', 'cb', 'cba']
    >>> good_subsequences('abbbcaaabcccaaabbbbbccab')
    ['', 'a', 'ab', 'abc', 'ac', 'acb', 'b', 'ba', 'bac',\
 'bc', 'bca', 'c', 'ca', 'cab', 'cb', 'cba']
    '''
    # Insert your code here
    index = ''
    flag = []
    for i in word:
        if i != index:
            index = i
            flag.append(i)
    result = []
    for i in range(0, len(set(flag)) + 1):
        for j in combinations(flag, i):
            if is_not_two_equal(j):
                result.append(j)
    flag.clear()
    for i in result:
        temp = ''
        for j in i:
            temp += j
        flag.append(temp)
    print(sorted(list(set(flag))))
# Possibly define another function
                

if __name__ == '__main__':
    import doctest
    doctest.testmod()
