def fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def febosencc(N):
    fibonacci_sequence = [fib(i) for i in range(1, N + 1)]
    return fibonacci_sequence


N = int(input())


result = febosencc(N)
print(*result)
