class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Etapa 1
        # criaria um dicionário para contar:
        #   chave: num; valor: qtde
        dicionario = {}

        # Etapa 2
        # validação de chave -> Verificar se o elemento existe ou não.
        #   existe: +1; não existe: criar a chave + 1  # .get()
        for num in nums:
            dicionario[num] = dicionario.get(num, 0) + 1

        # Etapa 3
        # ordenar o dicionário pelos valores em ordem decrescente
        # separar os top k valores.
        # .items() --> [(chave,valor),(num, qntd),...]
        nums_s = sorted(dicionario.items(),key = lambda x: x[1], reverse = True)
        # criar lista topk

        topk = [i[0] for i in nums_s[:k]]


        # Etapa fim 
        return topk