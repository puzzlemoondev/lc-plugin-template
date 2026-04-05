from typing import *
from leetcode.editor.common.node import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # variation of merging sorted array
        # two pointers from both end (negative squared is positive)
        # iterate the two and combine result
        n = len(nums)
        p_neg = 0
        p_pos = n - 1
        ans = [0] * n
        p = n - 1
        while p_neg <= p_pos:
            if abs(nums[p_neg]) <= abs(nums[p_pos]):
                ans[p] = nums[p_pos] ** 2
                p_pos -= 1
            else:
                ans[p] = nums[p_neg] ** 2
                p_neg += 1
            p -= 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    solution = Solution()
    # your test code here
