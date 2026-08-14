class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # estratégia de prefixos e sufixos
        # dividir o problema em duas partes e reduzir o Tempo de Complexidade
        # de O(n^2) -> O(3n) ~ O(n)

        # ler da esquerda para a direita (Produto dos Vz)

        # ler da direita para a esquerda (Produto Vz D)

        # Produto total dos vizinhos = Produto dos Vz E X Produto Vz D
        n = len(nums)
        pre = [1] * n
        suf = [1] * n

        prefixo = 1
        for i in range(n):
            pre[i] = prefixo
            prefixo *= nums[i] # <- Antes de seguir faço o produto prefixo + valor atual 
        
        sufixo = 1
        for i in range(n-1, -1, -1):
            suf[i] = sufixo
            sufixo *= nums[i]

        out = [pre[i] * suf[i] for i in range(n)]

        return out






