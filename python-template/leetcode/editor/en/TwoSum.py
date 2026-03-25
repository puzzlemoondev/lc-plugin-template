from typing import *
from leetcode.editor.common.node import *

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = [(v, i) for i, v in enumerate(nums)]
        pairs.sort()
        left, right = 0, len(nums) - 1
        while left < right:
            left_val, left_idx = pairs[left]
            right_val, right_idx = pairs[right]
            s = left_val + right_val
            if s == target:
                return [left_idx, right_idx]
            elif s < target:
                left += 1
            else:
                right -= 1
        return []
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()
    # your test code here
    print(solution.twoSum([3,2,4], 6))
    