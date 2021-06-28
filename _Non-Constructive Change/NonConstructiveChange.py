# Time O(nlog n), Space O(1)
def nonConstructibleChange(coins):

    # ensure that the incoming array is sorted
    coins.sort()

    currentChangeCreated = 0

    for coin in coins:
        if coin > currentChangeCreated + 1:
            return currentChangeCreated + 1

        currentChangeCreated += coin

    return currentChangeCreated + 1