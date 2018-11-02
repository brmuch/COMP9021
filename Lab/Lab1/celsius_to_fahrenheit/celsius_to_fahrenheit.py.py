
# coding: utf-8

'''
Prints out a conversion table of temperatures from Celsius to Fahrenheit degrees,
with the former ranging from 0 to 100 in steps of 10.
'''
min_temperature = 0
max_temperature = 100
step = 10
print('\tCelsius\tFahrenheit')

#change celsius to fahrenheit
for celsius in range(min_temperature, max_temperature + step, step):
    fahrenheit = 1.8*celsius+32
    print(f'{celsius:10}\t{fahrenheit:7.1f}')

