n=int(input())
lst=[]
for i in range(0,n):
    ele = input()
    lst.append(ele) 
    
if lst[n]==reversed(n):
    print('YES')
else:
    print('NO')
    