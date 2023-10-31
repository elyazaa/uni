#Printing Prime Numbers
print("Hello User ^^")
N = int(input("Please Enter Value of N: "))
print(f'Prime Numbers Up To {N} ...')
for number in range(2, N+1):
    sqrt = int(number ** 0.5) + 1
    for denominator in range(2, sqrt):
        if number % denominator == 0:
            break
    else:
        print(number, end=" ")