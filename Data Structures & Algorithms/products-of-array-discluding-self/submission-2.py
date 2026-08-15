class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        out = [1] * n

        prefixo = 1
        for i in range(n):
            out[i] = prefixo
            prefixo *= nums[i]
        
        sufixo = 1
        for i in range(n-1,-1,-1):
            out[i] *= sufixo
            sufixo *= nums[i]
        
        return out