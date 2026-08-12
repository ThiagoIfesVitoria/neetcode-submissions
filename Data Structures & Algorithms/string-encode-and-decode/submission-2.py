class Solution:
# padrão [tamanho]+[delimitador]+[palavra] 
# [Delimitador]: @

    def encode(self, strs: List[str]) -> str:
        # somar strings de forma iterativa - X
        # duplicação de memória 

        # criar uma lista com as palavras codificadas e no fim unir .join()

        lista = []

        for i in strs:
            enc = f"{len(i)}@{i}"
            lista.append(enc)

        return "".join(lista) # transforma tudo em string

    def decode(self, s: str) -> List[str]:

        i = 0
        lista = []
        #estrutura de repetição
        
        while i < len(s):
            j = i

            # encontrar delimitador
            while s[j] != "@":
                j += 1
            
            tamanho = int(s[i:j])
            palavra = s[j+1:j+1+tamanho]
            lista.append(palavra)
            i = j+1+tamanho

        return lista




