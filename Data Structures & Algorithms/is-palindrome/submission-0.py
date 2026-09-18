class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = "".join([char for char in s if char.isalnum()]).lower()
        head = 0
        tail = len(text) - 1
        while head <= tail:
            if text[head] != text[tail]:
                return False
            head +=1
            tail -=1

        return True