class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # slinding window
        i,j = 0,0

        elementos = set()
        sequencia = 0
        maior_sequencia = 0
        # loop no ponteiro exploratório
            # loop de contração de janela
        
        while j < len(s):

            if s[j] not in elementos:
                elementos.add(s[j])
                sequencia +=1
                maior_sequencia = max(maior_sequencia, sequencia)
                j+=1
            
            else:
                while s[j] in elementos:
                    elementos.remove(s[i])
                    sequencia -= 1
                    i+=1

        return maior_sequencia
