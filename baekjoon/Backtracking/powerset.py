n = 3
num = [1, 2, 3]
a = [0] * n  # 인덱스에 해당하는 원소를 부분집합에 포함할지 말지를 저장하는 배열

def powerset(k):
    # 모든 원소에 대해 선택 여부를 다 정했다면,
    if k == n:
        print([num[i] for i in range(n) if a[i]])
        return
    
    # num[k]를 선택한 경우
    a[k] = 1
    powerset(k+1)

    # num[k]를 선택하지 않은 경우
    a[k] = 0
    powerset(k+1)

powerset(0)