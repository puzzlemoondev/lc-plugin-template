from typing import *
from leetcode.editor.common.node import *
from collections import Counter


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        length = 0
        # a-z 26 kinds of characters
        for n in range(1, 27):
            length = max(length, self._longestSubStringNKinds(s, k, n))
        return length

    @staticmethod
    def _longestSubStringNKinds(s: str, k: int, n: int) -> int:
        freq = Counter()
        valid_chars = 0
        left = right = 0
        length = 0
        while right < len(s):
            c = s[right]
            freq[c] += 1
            if freq[c] == k:
                valid_chars += 1
            right += 1
            while len(freq) > n:
                d = s[left]
                if freq[d] == k:
                    valid_chars -= 1
                freq[d] -= 1
                if freq[d] == 0:
                    freq.pop(d)
                left += 1
            if valid_chars == n:
                length = max(length, right - left)
        return length


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    solution = Solution()
    # your test code here
