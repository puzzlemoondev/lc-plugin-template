from typing import *
from leetcode.editor.common.node import *

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n

        # Same two-pointer shape as RemoveDuplicatesFromSortedArray.py:
        # slow = index of the last kept element
        # fast = scans elements from left to right
        slow = 0
        fast = 1
        while fast < n:
            # Keep nums[fast] if:
            # 1) we have only kept one element so far (slow == 0), or
            # 2) nums[fast] differs from nums[slow - 1].
            #
            # Why compare with slow - 1:
            # if nums[fast] == nums[slow - 1], then the last two kept values
            # are both nums[fast], so adding this one would create a 3rd copy.
            if slow == 0 or nums[fast] != nums[slow - 1]:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1

        # slow is an index, so valid length is slow + 1.
        return slow + 1

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()
    # your test code here
    
