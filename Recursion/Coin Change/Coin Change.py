def coin_change(target, coins):
    # Default to target value
    min_coins = target
    # Check to see if we have a single coin match
    if target in coins:
        return 1
    else:
        # For every coin value that is <= target
        for i in [c for c in coins if c <=target]:
            # Recursively call (add a count coin and subtract from the target)
            num_coins = 1 + coin_change(target - i, coins)

            # Reset Minimum if we have a new minimum
            if num_coins < min_coins:
                min_coins = num_coins
    return min_coins

# print(coin_change(63,[1, 5, 10, 25]))

def coin_change_dynamic(target, coins, known_results):
    # Default to target value
    min_coins = target
    # Check to see if we have a single coin match
    if target in coins:
        known_results[target] = 1
        return 1
    # Return a known result if it happens to be greater than 1
    elif known_results[target] > 0:
        return known_results[target]
    else:
        # for every coin value that is <= than target
        for i in [c for c in coins if c <= target]:
            
            # Recursive call, note how we include the known results!
            num_coins = 1 + coin_change_dynamic(target-i,coins,known_results)
            
            # Reset Minimum if we have a new minimum
            if num_coins < min_coins:
                min_coins = num_coins
                
                # Reset the known result
                known_results[target] = min_coins
    return min_coins

target = 74
coins = [1,5,10,25]
known_results = [0]*(target+1)
print(coin_change_dynamic(target, coins, known_results))