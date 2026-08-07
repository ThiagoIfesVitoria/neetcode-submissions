class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # podemos utilizar a função counter()
        # podemos utilizar a Sorted() 
        return sorted(s) == sorted(t)