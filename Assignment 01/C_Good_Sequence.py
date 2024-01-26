mp={}

n = int(input())
int_val= list(map(int, input().split()))

for x in int_val:
    if x in mp:
        mp[x] += 1
    else:
        mp[x] = 1

cnt = 0

for u, freq in mp.items():
    if freq >= u:
        cnt += freq - u
    else:
        cnt += freq

print(cnt)
