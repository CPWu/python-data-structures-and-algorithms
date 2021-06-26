def balance_check(s):
    # If we know the the length of the input string than it would be impossible to be balanced.
    if len(s)%2 != 0:
        return False

    opening = set('([{')

    matches = set([('(',')'),('[',']'),('{','}')])

    stack = []

    for parenthesis in s:
        if parenthesis in opening:
            stack.append(parenthesis)
        else:
            if len(stack) == 0:
                return False
            
            last_open = stack.pop()

            if(last_open,parenthesis) not in matches:
                return False
    
    return len(stack) == 0



print(balance_check('[]'))

print(balance_check('[](){([[[]]])}'))

print(balance_check('()(){]}'))