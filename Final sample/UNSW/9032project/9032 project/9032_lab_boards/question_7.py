'''
Will be tested with height a strictly positive integer.
'''
def space(num):
    for i in range(0, num):
        print(" ",end = '')
 
def f(height):
    '''
    >>> f(1)
    0
    >>> f(2)
     0
    123
    >>> f(3)
      0
     123
    45678
    >>> f(4)
       0
      123
     45678
    9012345
    >>> f(5)
        0
       123
      45678
     9012345
    678901234
    >>> f(6)
         0
        123
       45678
      9012345
     678901234
    56789012345
    >>> f(20)
                       0
                      123
                     45678
                    9012345
                   678901234
                  56789012345
                 6789012345678
                901234567890123
               45678901234567890
              1234567890123456789
             012345678901234567890
            12345678901234567890123
           4567890123456789012345678
          901234567890123456789012345
         67890123456789012345678901234
        5678901234567890123456789012345
       678901234567890123456789012345678
      90123456789012345678901234567890123
     4567890123456789012345678901234567890
    123456789012345678901234567890123456789
    '''
    # Insert your code here
    start = 0
    for i in range(1, height + 1):
        space(height-1)
        for j in range(0, 2*i - 1):
            if start <= 9 and j != 2*i - 2:
                print(start,end= '')
            elif start <= 9 and j == 2*i - 2:
                print(start)
            elif start > 9 and j != 2*i - 2:
                start = 0
                print(start,end = '')
            elif start > 9 and j == 2* i - 2:
                start = 0
                print(start)
            start += 1
        height = height - 1
if __name__ == '__main__':
    import doctest
    doctest.testmod()
