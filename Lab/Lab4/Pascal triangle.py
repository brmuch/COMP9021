# Prompts the user for a number N and prints out the first N + 1 lines of Pascal triangle.
def print_space(num):
    for _ in range(0, num):
        print(" ", end = '')

def display_triangle(width,start_space):
    for i in range(0, len(pascal_triangle)):
        print_space(start_space)
        if i == 0:
            print(pascal_triangle[i][0])
        else:
            print(pascal_triangle[i][0], end='')

        for j in range(1, len(pascal_triangle[i])):
            print_space(2 * width - len(str(pascal_triangle[i][j])))
            if j == len(pascal_triangle[i]) - 1:
                print(pascal_triangle[i][j])
            else:
                print(pascal_triangle[i][j],end='')
        start_space = start_space - width


while True:
    try:
        N = int(input('Enter a nonnegative integer: '))
        if N < 0:
            raise ValueError
        break
    except ValueError:
        print('Incorrect input, try again')

pascal_triangle = []
triangle = [1]
pascal_triangle.append(triangle)

for _ in range(0, N):
    temp = [1]
    for i in range(1, len(triangle)):
        temp.append(triangle[i - 1] + triangle[i])
    temp.append(1)
    triangle = temp
    pascal_triangle.append(triangle)

width = len(str(pascal_triangle[N][N // 2]))
start_space = (1 + 2 * width * (len(pascal_triangle[-1]) - 1)) // 2 + width - 1
display_triangle(width,start_space)
