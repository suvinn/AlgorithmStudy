'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
전위, 중위, 후위 순회 결과
1 2 4 7 12 3 5 8 9 6 10 11 13 
12 7 4 2 1 8 5 9 3 10 6 13 11 
12 7 4 2 8 9 5 10 13 11 6 3 1 

13
2 1 2 3 1 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''
def pre_order(T):
    if T:
        print(T)
        pre_order(left[T])
        pre_order(right[T])

def in_order(T):
    if T:
        in_order(left[T])
        print(T)
        in_order(right[T])

def post_order(T):
    if T:
        post_order(left[T])
        post_order(right[T])
        print(T)

N = int(input())     # 1번부터 N번까지인 정점
E = N - 1            # 간선 수
arr = list(map(int, input().split()))

left = [0] * (N+1)   # 부모를 인덱스로 왼쪽 자식 저장
right = [0] * (N+1)  # 부모를 인덱스로 오른쪽 자식 저장
par = [0] * (N+1)    # 자식을 인덱스로 부모 저장

for i in range(E):
    p, c = arr[i*2], arr[i*2+1]
    par[c] = p
    if left[p] == 0:
        left[p] = c
    else:
        right[p] = c

print(left)
print(right)

root = 1
for i in range(1, N+1):
    if par[i] == 0:
        root = i
        break
pre_order(root)