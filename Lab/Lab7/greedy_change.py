# Prompts the user for an amount, and outputs the minimal number of banknotes
# needed to match that amount, as well as the detail of how many banknotes
# of each type value are used.
# The available banknotes have a face value which is one of
# $1, $2, $5, $10, $20, $50, and $100.


# Write by Ran Bai
value = [100, 50, 20, 10, 5, 2, 1]
banknotes = dict()

def recursive_cal_banknots(amount, index):
    if index == 6:
        if amount != 0:
            banknotes[1] = amount
        return
    else:
        if amount >= value[index]:
            banknotes[value[index]] = amount // value[index]
            recursive_cal_banknots(amount % value[index], index + 1)
        else:
            recursive_cal_banknots(amount, index + 1)
            
if __name__ == "__main__":
    amount = int(input("Input the desired amount: "))
    recursive_cal_banknots(amount, 0)
    print(f"\n{sum(banknotes.values())} {'banknote is' if sum(banknotes.values()) == 1 else 'banknotes are'} needed.")
    print("The detail is:")
    banknotes_key = sorted(banknotes.keys(), reverse = True)
    for key in banknotes_key:
        print(f"{' '*(3 - len(str(key)))}${key}: {banknotes[key]}")

