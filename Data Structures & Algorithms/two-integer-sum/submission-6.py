class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complemento_pos = {}

        for i in range(len(nums)): # Solução O(N)
            atual = nums[i]
            complemento = target - atual

            if complemento in complemento_pos:
                return [complemento_pos[complemento], i]

            complemento_pos[atual] = i