import time

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


def compare_algorithms(amount):
    print(f"\n=== Порівняння для суми {amount} ===")

    # Жадібний алгоритм
    start = time.time()
    greedy_result = find_coins_greedy(amount)
    greedy_time = time.time() - start
    greedy_total_coins = sum(greedy_result.values())  # Загальна кількість монет
    print(f"Жадібний алгоритм: {greedy_result}, загальна кількість монет: {greedy_total_coins}, час: {greedy_time:.6f} сек")

    # Динамічне програмування
    start = time.time()
    dp_result = find_min_coins(amount)
    dp_time = time.time() - start
    dp_total_coins = sum(dp_result.values())  # Загальна кількість монет
    print(f"Динамічне програмування: {dp_result}, загальна кількість монет: {dp_total_coins}, час: {dp_time:.6f} сек")

if __name__ == "__main__":   
    compare_algorithms(113)
    compare_algorithms(378)
    compare_algorithms(999)
    compare_algorithms(10000)
    compare_algorithms(37033)