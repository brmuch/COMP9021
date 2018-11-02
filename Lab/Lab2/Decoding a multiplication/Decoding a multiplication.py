# Decodes all multiplications of the form
#
#                        *  *  *
#                   x       *  *
#                     ----------
#                     *  *  *  *
#                     *  *  *
#                     ----------
#                     *  *  *  *
#
# such that the sum of all digits in all 4 columns is constant.


# Insert your code here.


for x in range(100, 1_000):
    for y in range(10, 100):
	
        #columnsi is the sum of all digits in columns i
        columns1 = ((x*y)//1000)*2
        columns2 = (int(str(x*y)[1]))*2+x//100
        columns3 = (int(str(x*y)[2]))*2 + y//10 + (int(str(x)[1]))
        columns4 = ((x*y)%10)*2+x%10+y%10
        
        if (y%10)*x in range(1000, 10_000):
            if (y//10)*x in range(100, 1_000):
                if (x * y) in range(1_000, 10_000) and (
                        columns1 == columns2 and columns3 == columns4 and columns1 == columns3):
                    print(f"{x} * {y} = {x*y}, all columns adding up to {((x*y)//1000)*2}.")