import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

for _ in range(int(input())):
    k = int(input())
    arr_minheap, arr_maxheap, dct = [], [], defaultdict(int)
    for _ in range(k):
        s, n = input().split()
        if s == 'I':
            dct[int(n)] += 1
            heapq.heappush(arr_minheap, int(n))
            heapq.heappush(arr_maxheap, -int(n))
        else:
            # minheap arr에서 최솟값 삭제
            if n == '-1':
                while arr_minheap:
                    min_v = heapq.heappop(arr_minheap)
                    if dct[min_v]:
                        dct[min_v] -= 1
                        break
            # maxheap arr에서 최댓값 삭제
            else:
                while arr_maxheap:
                    max_v = -heapq.heappop(arr_maxheap)
                    if dct[max_v]:
                        dct[max_v] -= 1
                        break
    while arr_minheap and dct[arr_minheap[0]] == 0:
        heapq.heappop(arr_minheap)
    while arr_maxheap and dct[-arr_maxheap[0]] == 0:
        heapq.heappop(arr_maxheap)
    if not arr_minheap or not arr_maxheap:
        print('EMPTY')
    else:
        print(-arr_maxheap[0], arr_minheap[0])