N = int(input())
arr = []
check = []
count = 0
operator = []
for _ in range(N):
    arr.append(int(input()))
    
for i in range(1,N+1):
    check.append(i)
check.reverse()

curr = []

while curr or check :
    if count == N:
        break
    
    
    if not curr or arr[count] != curr[-1] :
        if not check :
            break
        curr.append(check.pop())
        operator.append("+")
        
    else :
        count += 1
        operator.append("-")
        curr.pop()
    

if count == N :
    for j in operator :
        print(j)

else :
    print("NO")



