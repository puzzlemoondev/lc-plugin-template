from typing import *
from collections import Counter
from leetcode.editor.common.node import *

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # required char counts, needs a counter because t can have duplicates
        needs = Counter(t)
        # current window counter state
        window = Counter()

        left = right = 0 # [left, right)
        valid_chars = 0 # number of chars with count satisfying need
        start = 0 # start index of res
        length: int | None = None # length of res

        while right < len(s):
            # char to put into window
            c = s[right]
            # INCREASE WINDOW
            right += 1
            # UPDATE WINDOW
            if c in needs:
                window[c] += 1
                if window[c] == needs[c]:
                    valid_chars += 1

            # check window needs decreasing
            while valid_chars == len(needs):
                # current window length
                new_length = right - left
                # update min length if needed
                if length is None or new_length < length:
                    start = left
                    length = new_length

                # char to remove from window
                d = s[left]
                # DECREASE WINDOW
                left += 1
                # UPDATE WINDOW AFTER DECREASE
                if d in needs:
                    if window[d] == needs[d]:
                        valid_chars -= 1
                    window[d] -= 1

        return s[start:start+length] if length else ""
        
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()
    # your test code here
    