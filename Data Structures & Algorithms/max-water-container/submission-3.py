class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0 
        j = len(heights) - 1

        maior_area = 0

        while i < j:
            area = min(heights[i], heights[j]) * (j - i)

            if area >= maior_area:
                maior_area = area
            
            if heights[i] < heights[j]:
                i += 1

            elif heights[j] < heights[i]:
                j -= 1
            
            else:
                if heights[j-1] > heights[j]:
                    j-=1
                    
                else:
                    i+=1
        
        return maior_area