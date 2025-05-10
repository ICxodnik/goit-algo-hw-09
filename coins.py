def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}

    for coin in coins:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount -= coin * count

    return result

def find_min_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]
    memo = {}

    def dp(remaining):
        if remaining == 0:
            return {}
        if remaining in memo:
            return memo[remaining]

        min_combination = None

        for coin in coins:
            if coin <= remaining:
                sub_result = dp(remaining - coin)
                if sub_result is not None:
                    candidate = sub_result.copy()
                    candidate[coin] = candidate.get(coin, 0) + 1

                    if (min_combination is None or 
                        sum(candidate.values()) < sum(min_combination.values())):
                        min_combination = candidate

        memo[remaining] = min_combination
        return min_combination

    return dp(amount)
