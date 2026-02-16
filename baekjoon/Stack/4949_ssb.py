while True:
    stack = []
    sen = input()
    if sen == '.':
        break

    for s in sen:
        if s == '(':
            stack.append(')')
        elif s == '[':
            stack.append(']')
        elif s == ')':
            if not stack:
                ans = 'no'
                break
            tmp = stack.pop()
            if s != tmp:
                ans = 'no'
                break
        elif s == ']':
            if not stack:
                ans = 'no'
                break
            tmp = stack.pop()
            if s != tmp:
                ans = 'no'
                break
    else:
        if stack:
            ans = 'no'
        else:
            ans = 'yes'
    
    print(ans)