from typing import *
from leetcode.editor.common.node import *

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix, suffix = [1] * (n + 1), [1] * (n + 1)
        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1] * nums[i - 1]
            suffix[n - i] = suffix[n - i + 1] * nums[n - i]
        res = []
        for i in range(1, n + 1):
            res.append(prefix[i - 1] * suffix[i])
        return res
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()
    # your test code here
    