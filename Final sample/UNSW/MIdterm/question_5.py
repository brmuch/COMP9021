'''
Will be tested with year between 1913 and 2013.
You might find the reader() function of the csv module useful,
but you can also use the split() method of the str class.
'''

import csv
import sys
import re
def f(year):
    '''
    >>> f(1914)
    In 1914, maximum inflation was: 2.0
    It was achieved in the following months: Aug
    >>> f(1922)
    In 1922, maximum inflation was: 0.6
    It was achieved in the following months: Jul, Oct, Nov, Dec
    >>> f(1995)
    In 1995, maximum inflation was: 0.4
    It was achieved in the following months: Jan, Feb
    >>> f(2013)
    In 2013, maximum inflation was: 0.82
    It was achieved in the following months: Feb
    '''
    months = 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
    # Insert your code here
    filename = 'cpiai.csv'
    max_inflation = 0
    month = []
    
    f = open(filename,'r')
    f.readline()
    for line in f.readlines():
        text = re.split(r',', line)
        date = re.split(r'-', text[0])
        if int(date[0]) == year and float(text[2]) > max_inflation:
            max_inflation = float(text[2])
            month.clear()
            month.append(int(date[1]))
        elif int(date[0]) == year and float(text[2]) == max_inflation:
            month.append((date[1]))

    print(f"In {year}, maximum inflation was: {max_inflation}")    
    print(f"It was achieved in the following months: ",end = '')

    for i in range(0, len(month)):
        if i == len(month) - 1:
            print(f"{months[int(month[i]) - 1]}")
        else:
            print(f"{months[int(month[i]) - 1]}, ", end ='')
if __name__ == '__main__':
    import doctest
    doctest.testmod()
