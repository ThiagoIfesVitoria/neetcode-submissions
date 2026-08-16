class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # iniciar os ponteiros
        i=0 # dia 0
        j=1 # um dia após
        
        max_profit = 0

        while j < len(prices): # enquanto não chegar no fim da pesquisa

            v_compra = prices[i]
            v_venda = prices[j]

            if v_compra < v_venda: # aqui temos lucro
                lucro = v_venda - v_compra  
                max_profit = max(lucro, max_profit) #ver se o lucro é global
            
            else: # aqui encontramos uma oportunidade de compra
                i = j
            
            j+=1 # continua com nossa pesquisa de mercado
        
        return max_profit
