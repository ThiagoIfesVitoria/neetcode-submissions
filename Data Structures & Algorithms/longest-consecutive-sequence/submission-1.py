class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # complexidade O(n)
        # [2,20,4,10,3,4,5]

        n = len(nums)
        if n == 0:
            return 0

        num_set = set(nums)
        sequencia = 1
        maior_sequencia = 1

        for num in num_set:
            if num - 1 not in num_set: # É o início de uma sequencia
                while num + sequencia in num_set:
                    sequencia+=1
                    if sequencia >= maior_sequencia:
                        maior_sequencia = sequencia
                sequencia = 1
        
        return maior_sequencia
