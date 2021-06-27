def pair_sum(array, k):
    if len(array)<2:
        return
    
    # Sets for tracking
    seen = set()
    output = set()

    for num in array:
        target = k - num

        if target not in seen: 
            seen.add(num)
        else:
            output.add( ((min(num,target)), max(num,target)))

    #return len(output)
    print ('\n' .join(map(str,list(output))))

print(pair_sum([1,2,2],4))