from typing import *
from leetcode.editor.common.node import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Because nums is sorted, all duplicates are adjacent.
        # We can compact unique values in-place with two pointers.
        n = len(nums)
        if n <= 1:
            return n

        # slow: index of the last unique value already placed.
        # fast: scans every element from left to right.
        fast = slow = 0
        while fast < n:
            # When we find a new value, move slow forward and write it there.
            if nums[fast] != nums[slow]:
                # slow points to the last unique value, so the new unique value
                # must be written at the next index (slow + 1), not current slow.
                slow += 1
                nums[slow] = nums[fast]
            fast += 1
        # slow is an index, so the number of unique elements is slow + 1.
        return slow + 1


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    solution = Solution()
    # your test code here
