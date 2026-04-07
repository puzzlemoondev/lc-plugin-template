from typing import *
from leetcode.editor.common.node import *

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        preSum = [0] * (n + 1)
        for i in range(n):
            # map 0 to -1. we want to find the max preSum len with the sum being 0
            preSum[i + 1] = preSum[i] + (-1 if nums[i] == 0 else 1)
        val_to_index = {}
        res = 0
        for i in range(len(preSum)):
            val = preSum[i]
            j = val_to_index.get(val, None)
            if j is not None:
                res = max(res, i - j)
            else:
                val_to_index[val] = i
        return res
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()
    # your test code here
    