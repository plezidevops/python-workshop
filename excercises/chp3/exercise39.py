numbers = [7, 50, 6,5]

maximum = 0

for n in numbers:
    if n > maximum:
        maximum = n
    print(n)

print(f'The maximum number is: {maximum}')