from typing import List


def maxProfit(prices: List[int]) -> int:

    i = 0
    j = 1
    k = 1
    buy = prices[i]

    while j < len(prices):  ## review to do in an only loop
        if prices[j] < prices[i]:
            buy = prices[j]
            k = j + 1
            break
        i += 1
        j += 1

    print(k)
    sell = prices[j]

    while k < len(prices):
        if prices[k] > prices[j]:
            sell = prices[k]
            break
        j += 1
        k += 1

    return max(sell - buy, 0)


# print(maxProfit([7, 1, 5, 3, 6, 4]))
# print(maxProfit([7, 6, 4, 3, 1]))
print(maxProfit([1, 2]))
