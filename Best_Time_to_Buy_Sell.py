from typing import List


def maxProfit(prices: List[int]) -> int:

    len_prices = len(prices)
    if len_prices < 2:
        return 0
    i, j, k = 0, 1, 1

    buy = prices[i]
    sell = prices[j]

    while j < len_prices:
        if prices[j] < prices[i]:
            buy = prices[j]
            k = j + 1
            break
        i += 1
        j += 1
    print(buy)

    print(i, j, k)
    while k < len_prices:
        if prices[k] > buy and prices[k] > sell:
            sell = prices[k]

        k += 1
    print(k)

    print(sell)
    return max(sell - buy, 0)


print(f"El profit is {maxProfit([7, 1, 5, 3, 6, 4])}")
print(f"El profit is {maxProfit([7, 6, 4, 3, 1])}")
print(f"El profit is {maxProfit([1, 2])}")
print(f"El profit is {maxProfit([1, 2, 4])}")
print(f"El profit is {maxProfit([1, 4, 2])}")
