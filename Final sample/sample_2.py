banknotes = {}
banknote_values = [1, 2, 5, 10, 20, 50, 100]
def recursive_method(num, amount):
    if num == 0:
        if amount > 0:
            banknotes[1] = amount
        return
    else:
        if amount >= banknote_values[num]:
            banknotes[banknote_values[num]] = amount // banknote_values[num]
            recursive_method(num - 1, amount % banknote_values[num])
        else:
            recursive_method(num - 1, amount)
def f(N):
    '''
    >>> f(20)
    Here are your banknotes:
    $20: 1
    >>> f(40)
    Here are your banknotes:
    $20: 2
    >>> f(42)
    Here are your banknotes:
    $2: 1
    $20: 2
    >>> f(43)
    Here are your banknotes:
    $1: 1
    $2: 1
    $20: 2
    >>> f(45)
    Here are your banknotes:
    $5: 1
    $20: 2
    >>> f(2537)
    Here are your banknotes:
    $2: 1
    $5: 1
    $10: 1
    $20: 1
    $100: 25
    '''
    banknote_values = [1, 2, 5, 10, 20, 50, 100]
    # Insert your code here
    print('Here are your banknotes:')
    banknotes.clear()
    recursive_method(6, N)
    keys = sorted(banknotes.keys())
    for key in keys:
        print(f"${key}: {banknotes[key]}")

if __name__ == '__main__':
    import doctest
    doctest.testmod()
