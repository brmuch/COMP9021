# Finds all triples of positive integers (i, j, k) such that
# i, j and k are two digit numbers, i < j < k,
# every digit occurs at most once in i, j and k,
# and the product of i, j and k is a 6-digit number
# consisting precisely of the digits that occur in i, j and k.

result = set()
for i in range(10, 100):
    for j in range(10, 100):
        for k in range(10,100):
            if i!=j and i!=k and j!=k:
                num_list = set()
                num_list.add(i//10)
                num_list.add(i%10)
                num_list.add(j // 10)
                num_list.add(j % 10)
                num_list.add(k // 10)
                num_list.add(k % 10)
                if len(num_list) != 6:
                    continue
                lists = [int(str(i*j*k)[_]) for _ in range(0, len(str(i*j*k)))]
                flag = 0
                if len(num_list) != len(lists):
                    flag = 1
                for m in num_list:
                    if m not in lists:
                        flag = 1
                        break
                if flag == 0 and i*j*k not in result:
                    print(f"{i} x {j} x {k} = {i*j*k} is a solution.")
                    result.add(i*j*k)