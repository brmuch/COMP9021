import sys
import os
import csv
import re
import string

filename = 'HNP_Data.csv'
if not os.path.exists(filename):
    print(f'There is no file named {filename} in the working directory, giving up...')
    sys.exit()

indicator_of_interest = input('Enter an Indicator Name: ')
records = []
max_value = None
countries_for_max_value_per_year = dict()
first_year = 1960

try:
    f = open(filename, 'r')
    f.readline()
    for line in f.readlines():
        list = re.split(r",", line.strip('\n').strip(' '))
        if '"' in list[2]:
            while '"' not in list[3]:
                list[2] += ',' + list[3]
                list.pop(3)
            list[2] += ',' + list[3]
            list.pop(3)
        if '"' in list[0]:
            while '"' not in list[1]:
                list[0] += ',' + list[1]
                list.pop(1)
            list[0] += ',' + list[1]
            list.pop(1)

        if list[2].strip('\'').strip('\"') == indicator_of_interest:
            for i in range(4, len(list)):
                if list[i] != '':
                    if max_value == None:
                        max_value = float(list[i])
                    elif max_value < float(list[i]):
                        max_value = float(list[i])
                        countries_for_max_value_per_year.clear()

                    if max_value != None and float(list[i]) == max_value:
                        if first_year + i - 4 in countries_for_max_value_per_year.keys():
                            countries_for_max_value_per_year[first_year + i - 4].append(list[0].replace("\"", ''))
                        else:
                            countries_for_max_value_per_year[first_year + i - 4] = [list[0].replace("\"", '')]
    f.close()
except IOError:
    sys.exit()

max_value = int(max_value) if max_value != None and max_value == int(max_value) else max_value
if max_value == None:
    print('Sorry, either the indicator of interest does not exist or it has no data.')
else:
    print('The maximum value is:', max_value)
    print('It was reached in these years, for these countries or categories:')
    for year in sorted(countries_for_max_value_per_year):
        print(f'    {year}: {countries_for_max_value_per_year[year]}')