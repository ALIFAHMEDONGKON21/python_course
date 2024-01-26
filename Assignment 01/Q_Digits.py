
t = int(input())

for _ in range(t):

    n = int(input())

    digits = [int(digit) for digit in str(n)][::-1]

    print(*digits)
