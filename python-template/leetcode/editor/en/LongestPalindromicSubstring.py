from typing import *
from leetcode.editor.common.node import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        for i in range(len(s)):
            ans_odd = self._palindrome(s, i, i)
            ans_even = self._palindrome(s, i, i + 1)
            len_ans_odd = len(ans_odd)
            len_ans_even = len(ans_even)
            ans_candidate = ans_odd if len_ans_odd > len_ans_even else ans_even
            if len(ans_candidate) > len(ans):
                ans = ans_candidate
        return ans

    @staticmethod
    def _palindrome(s: str, left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1 : right]


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    solution = Solution()
    # your test code here
