class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Eu posso escolher não realizar transações. (return 0)
        # Eu preciso escolher um início e um fim(futuro)
        # Return é o meu lucro máximo.
        max_profit = 0
        for i in range(len(prices)):
            for j in range(len(prices)):
                if j > i:
                    profit = prices[j] - prices[i]
                    max_profit = max(profit, max_profit)

        max_profit = max_profit if max_profit > 0 else 0

        return max_profit


