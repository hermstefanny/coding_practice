from typing import List


def maxProfit(prices: List[int]) -> int:

    len_prices = len(prices)
    if len_prices <= 1:
        return 0
    i = 0
    win = 0

    while i < len_prices - 1:
        j = i + 1
        while j < len_prices:
            possible_win = prices[j] - prices[i]
            if possible_win > win:
                win = possible_win
            j += 1
        i += 1

    return max(win, 0)


print(maxProfit([7, 1, 5, 3, 6, 4]))
print(maxProfit([7, 6, 4, 3, 1]))
print(maxProfit([1, 2]))
print(maxProfit([1, 2, 4]))
print(maxProfit([1, 4, 2]))
