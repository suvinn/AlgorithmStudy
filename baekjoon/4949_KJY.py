while True :
    line = input()
    if line == "." :
        break
    
    stack = []

    for j in line:
        if j not in "()[]" :
            continue

        if j in "([" :
            stack.append(j)
            
        if j in ")]" :
            if not stack :
                print("no")
                break

            if (stack[-1] == "(" and j == ")") or (stack[-1] == "[" and j == "]"):
                stack.pop()

            else:
                print("no")
                break
    
    else :
        if stack :
            print("no")

        else :
            print("yes")    
