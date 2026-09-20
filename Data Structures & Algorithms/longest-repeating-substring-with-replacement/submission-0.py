from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count= Counter()
        left = best = max_count = 0
        for right, ch in enumerate(s):
            count[ch] += 1
            max_count = max(max_count, count[ch])

            while (right-left + 1) - max_count > k:
                count[s[left]] -=1
                left +=1
            best = max(best, right - left + 1)
        return best 