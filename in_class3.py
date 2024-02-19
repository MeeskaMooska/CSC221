
numbers = [-9, 1, 6, 10]
for position, number in enumerate(numbers):
    if number < 0:
        print(f'{position} {number}')
    else:
        print(f'{position} x')