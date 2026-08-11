class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        topk = {}
        for num in nums:
            if num not in topk:
                topk[num] = 1
            topk[num] = topk[num] + 1

        topks = sorted(topk.items(), key = lambda item: item[1], reverse = True) # <--hacker
        top = []
        for item in topks:
            top.append(item[0])

        return top[0:k]