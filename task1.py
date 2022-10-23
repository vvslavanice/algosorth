'''

Task 1

'''


def bubblemethod(number):
    n = len(number)

    for i in range(n):
        for ix in range(0, n - i - 1):
            if number[ix] > number[ix + 1]:
                number[ix], number[ix + 1] = number[ix + 1], number[ix]

number = [1, 2, 3, 4, 5, 6]
bubblemethod(number)
for i in range(len(number)):
    print(number[i])