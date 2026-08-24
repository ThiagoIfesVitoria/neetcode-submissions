class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        par = {
            "]":"[",
            "}":"{",
            ")":"("
        }

        for brk in s:
            if brk in ["[","{","("]:
                stack.append(brk)

            else:
                if len(stack) == 0:
                    return False
                    
                brk_f = par.get(brk)
                if brk_f == stack[-1]:
                    stack.remove(brk_f)
                
                else: #estou fechando fora de ordem
                    return False
        
        if len(stack) == 0:
            return True

        else:
            return False 