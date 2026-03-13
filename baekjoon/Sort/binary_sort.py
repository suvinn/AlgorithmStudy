arr = [12, 2, 7, 9, 23, 11, 3]
# [주의!] 이진 검색은 항상 정렬된 데이터에 적용
arr.sort()

def binary_search_while(target):
    left = 0                 # 검색 시작점
    right = len(arr) - 1     # 검색 끝점
    cnt = 0                  # 검색 횟수

    while left <= right:
        mid = (left + right) // 2
        cnt += 1

        # 정답을 찾으면 종료
        if arr[mid] == target:
            return mid
        
        # arr[mid]가 target보다 더 큰 경우 (target이 왼쪽에 위치)
        # - 왼쪽을 탐색
        if target < arr[mid]:
            right = mid - 1
        # arr[mid]가 target보다 더 작은 경우 (target이 오른쪽에 위치)
        # - 오른쪽을 탐색
        else:
            left = mid + 1
    
    return -1