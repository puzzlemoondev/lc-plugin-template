from typing import List
from collections import Counter

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res: List[int] = []

        needs = Counter(p)
        window = Counter()

        left = right = 0 # [left,right)
        valid_chars = 0

        while right < len(s):
            c = s[right]
            # INCREASE WINDOW
            right += 1
            # UPDATE WINDOW
            if c in needs:
                window[c] += 1
                if window[c] == needs[c]:
                    valid_chars += 1

            while right - left >= len(p):
                if valid_chars == len(needs):
                    res.append(left)
                # DECREASE WINDOW
                d = s[left]
                left += 1
                # UPDATE WINDOW
                if d in needs:
                    if window[d] == needs[d]:
                        valid_chars -= 1
                    window[d] -= 1

        return res
        
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()
    # your test code here
    