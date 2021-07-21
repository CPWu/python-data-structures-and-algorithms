def balance_check(s):
    # If we know the the length of the input string than it would be impossible to be balanced.
    if len(s)%2 != 0:
        return False

    dic = {'{':'}','[':']','(':')'}
    lst =[]
    for i in s:
        if i in dic.keys():
            lst.append(dic[i])
        elif len(lst)>0 and i==lst[-1]:
            lst.pop()
        else: 
            return False
    return len(lst) == 0



print(balance_check('[]'))

print(balance_check('[](){([[[]]])}'))

print(balance_check('()(){]}'))