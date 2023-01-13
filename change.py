'''
Correctly determine the fewest number of coins to be given to a customer such that the sum of the coins' value would equal the correct amount of change.

For example
An input of 15 with [1, 5, 10, 25, 100] should return one nickel (5) and one dime (10) or [5, 10]
An input of 40 with [1, 5, 10, 25, 100] should return one nickel (5) and one dime (10) and one quarter (25) or [5, 10, 25]
'''

def find_fewest_coins(coins, target):
    fewest_coins = []

    if target < 0:
        raise ValueError("target can't be negative")

    err = [i for i in coins if i <= target]
    if not err and target != 0:
        raise ValueError("can't make target with given coins")

    if target in coins:
        fewest_coins.append(target)
        return fewest_coins

    coins_change = list(filter(lambda x: x < target, coins))
    coins_change.reverse()
    coins_change_v2 = coins_change.copy()
    coins_change_v3 = coins_change.copy()

    if len(coins_change) > 3:
        v1 = count_coins(coins_change, target)
        v1.reverse()
        v2 = count_coins(coins_change_v2[1:], target)
        if sum(v2) != target:
            v2 = []
            #print("entreee", v2)
            for i in coins_change_v3[1:]:
                v2.append(i)
            #print("entreee", v2)
            
            while coins_change_v3:
                if sum(v2) == target:
                    break
                if coins_change_v3[0] + sum(v2) > target:
                    coins_change_v3.pop(0)
                else:
                    v2.append(coins_change_v3[0])

        v2.reverse()
        #print("result", sum(v1), sum(v2), target)
        if sum(v1) != target and sum(v2) != target:
            raise ValueError("can't make target with given coins")
        return v1 if (sum(v1) == target and sum(v2) == target) and len(v1) < len(v2) else v2
    else:
        v1 = count_coins(coins_change, target)
        v1.reverse()
        if sum(v1) != target:
            raise ValueError("can't make target with given coins")

    return v1

def count_coins(coins, target):
    fewest_coins = []

    while sum(fewest_coins) != target:
        if len(coins) == 0:
            return fewest_coins

        #print("Change", coins)
        if (coins[0] > sum(fewest_coins) and sum(fewest_coins) != 0) or coins[0] + sum(fewest_coins) > target:
            coins.pop(0)
            continue

        fewest_coins.append(coins[0])
        #print("Fewest", fewest_coins)

        if sum(fewest_coins) == target:
            return fewest_coins

        if len(coins) > 1:
            if (target - sum(fewest_coins)) % coins[1] == 0:
                #print("hola", target - sum(fewest_coins))
                for i in range(target // coins[1]):
                    if sum(fewest_coins) == target:
                        return fewest_coins
                    fewest_coins.append(coins[1])
                return fewest_coins

    return fewest_coins

if __name__ == "__main__":
    # print(find_fewest_coins([1, 5, 10, 25], 1)) #[1]
    # print(find_fewest_coins([1, 5, 10, 21, 25], 63)) #[21, 21, 21]
    # print(find_fewest_coins([1, 5, 10, 25, 100], 15)) #[5, 10]
    # print(find_fewest_coins([1, 5, 10, 25, 100], 25)) #[25]
    # print(find_fewest_coins([1, 4, 15, 20, 50], 23)) #[4, 4, 15]
    # print(find_fewest_coins([1, 2, 5, 10, 20, 50, 100], 999)) #[2, 2, 5, 20, 20, 50, 100, 100, 100, 100, 100, 100, 100, 100, 100]
    # print(find_fewest_coins([4, 5], 27)) #[4, 4, 4, 5, 5, 5]
    # print(find_fewest_coins([1, 5, 10, 21, 25], 0)) #[]
    #print(find_fewest_coins([5, 10], 3)) #can't make target with given coins
    #print(find_fewest_coins([5, 10], 94)) #can't make target with given coins
    #print(find_fewest_coins([5, 10], -94)) #target can't be negative
    print(find_fewest_coins([2, 5, 10, 20, 50], 21)) #[2, 2, 2, 5, 10]
