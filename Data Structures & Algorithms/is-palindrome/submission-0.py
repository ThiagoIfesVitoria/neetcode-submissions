class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Estratégia Two  Pointers
        s = s.lower()
        s_l = [car for car in s if car.isalnum()]

        i = 0 # coloca o ponteiro no início
        j = len(s_l) - 1 # coloca o ponteiro no final
        while i < j: # enquanto os ponteiros não se cruzarem
            if s_l[i] != s_l[j]: # checar se é um palindromo
                return False
            
            i += 1 # ando com o ponteiro ->
            j -= 1 # ando com o ponteir <-
        
        return True