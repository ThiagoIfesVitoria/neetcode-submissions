class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0 
        j = len(heights) - 1

        maior_area = 0

        while i < j:
            area = min(heights[i], heights[j]) * (j - i)

            if area >= maior_area: # posso substituir por max()
                maior_area = area
            
            if heights[i] < heights[j]:
                i += 1

            else:
                j -= 1
        
        return maior_area