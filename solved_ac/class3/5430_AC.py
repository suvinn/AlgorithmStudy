import sys
input = sys.stdin.readline

# R: 배열에 있는 수의 순서를 뒤집는 함수
# D: 첫 번째 수를 버리는 함수, 배열이 비어있는데 D를 사용한 경우에는 에러가 발생한다.

T = int(input())
for _ in range(T):
    p = input().strip()
    n = int(input())
    if n == 0:
        tmp = input()
        x_list = []
    else:
        x_list = input().strip()[1:-1].split(',')
    
    r = 0
    left, right = 0, n
    for func in p:
        if func == 'R':
            r += 1
        else:
            if r % 2 == 0:
                left += 1
            else:
                right -= 1
    
    if left > right:
        print('error')
    else:
        if r % 2 == 0:
            print('[' + ','.join(x_list[left:right]) + ']')
        else:
            print('[' + ','.join(x_list[left:right][::-1]) + ']')


# from collections import deque

# # R: 배열에 있는 수의 순서를 뒤집는 함수
# # D: 첫 번째 수를 버리는 함수, 배열이 비어있는데 D를 사용한 경우에는 에러가 발생한다.

# T = int(input())
# for _ in range(T):
#     p = input()
#     n = int(input())
#     if n == 0:
#         tmp = input()
#         x_list = deque([])
#     else:
#         x_list = deque(input()[1:-1].split(','))

#     flag = False
#     for func in p:
#         if func == 'R':
#             x_list.reverse()
#         else:
#             if not x_list:
#                 print('error')
#                 flag = True
#                 break
#             else:
#                 x_list.popleft()
#         if flag:
#             break
#     else:
#         print('[' + ','.join(x_list) + ']')