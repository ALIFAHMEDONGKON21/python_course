def m_op(n, arr):
    mn_op = float('inf')

    for num in arr:
        op = 0
        while num % 2 == 0 and num > 0:
            op += 1
            num //= 2

        mn_op = min(mn_op, op)

    return mn_op

n = int(input())
arr = list(map(int, input().split()))

res= m_op(n, arr)
print(res)
