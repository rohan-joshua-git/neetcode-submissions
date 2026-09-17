class Solution:
    def isValid(self, s: str) -> bool:
        matcher = {")": "(", "]": "[", "}": "{"}

        stack = []
        for b in s:
            if b in matcher.values():
                stack.append(b)
            else:
                if stack == []:
                    return False
                if (stack[-1] != matcher[b]):
                    return False
                stack.pop()
        
        if stack:
            return False
        
        return True