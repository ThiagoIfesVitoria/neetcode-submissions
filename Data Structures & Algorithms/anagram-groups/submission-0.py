class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicionario = {}

        for st in strs:
            anagram = "".join(sorted(st))
            if anagram in dicionario:
                dicionario[anagram].append(st)
            else:
                dicionario[anagram] = [st]

        return list(dicionario.values())
