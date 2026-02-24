cnt = 0  # 방문 순서 (지금까지 몇 개의 노드를 방문했는지)
def inorder(T):  # T: 현재 노드 번호
    global cnt

    # 배열 범위를 벗어나면 → 존재하지 않는 노드 → 재귀 종료
    if T > N:
        return
    
    # 왼쪽 서브트리 먼저 방문
    inorder(T*2)
    cnt += 1
    tree[T] = cnt
    inorder(T*2 + 1)

for tc in range(1, int(input())+1):
    N = int(input())
    tree = [0] * (N + 1)
    inorder(1)  # 완전 이진 트리의 루트는 1