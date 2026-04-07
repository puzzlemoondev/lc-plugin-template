from typing import *
from leetcode.editor.common.node import *

# leetcode submit region begin(Prohibit modification and deletion)
class NumArray:
    def __init__(self, nums: List[int]):
        self.pre_sum = self._calculate_pre_sum(nums)

    def sumRange(self, left: int, right: int) -> int:
        return self.pre_sum[right + 1] - self.pre_sum[left]

    @staticmethod
    def _calculate_pre_sum(nums: List[int]) -> List[int]:
        n = len(nums)
        pre_sum: List[int] = [0] * (n + 1)
        for i in range(1, n + 1):
            pre_sum[i] = pre_sum[i - 1] + nums[i - 1]
        return pre_sum

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return -1
        num_arr = NumArray(nums)
        for i in range(n):
            left_sum = num_arr.sumRange(0, i - 1) if i > 0 else 0
            right_sum = num_arr.sumRange(i + 1, n - 1) if i < n - 1 else 0
            if left_sum == right_sum:
                return i
        return -1
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()
    # your test code here
    