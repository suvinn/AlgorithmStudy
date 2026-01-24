while True:
    num = input()
    if int(num) == 0:
        break
    if len(num)%2 == 0:
        num1 = num[:len(num)//2]
        num2 = num[len(num)//2:]
    else:
        num1 = num[:len(num)//2]
        num2 = num[len(num)//2+1:]
    if num1 == num2[::-1]:
        print('yes')
    else:
        print('no')