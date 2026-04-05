from typing import *
from leetcode.editor.common.node import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Standard Dutch National Flag pointers:
        # arr[0 .. low - 1] → All 0s
        # arr[low .. mid - 1] → All 1s
        # arr[mid .. high] → Unprocessed elements (unknown)
        # arr[high + 1 .. n - 1] → All 2s
        low = 0
        mid = 0
        high = len(nums) - 1

        # process elements until mid crosses high (high not yet processed)
        while mid <= high:
            if nums[mid] == 0:
                # Put 0 into the left zone, then advance both low and mid.
                # After swap, index low is finalized as 0.
                # The value moved to mid comes from [low, mid): it is 1
                # (or the same index when low == mid), so mid is safe to advance.
                self._swap(nums, low, mid)
                low += 1
                mid += 1
            elif nums[mid] == 1:
                # 1 belongs to [low, mid), and swapping is unnecessary.
                # Since low only tracks where 0s end, moving mid forward
                # keeps all interval invariants valid.
                mid += 1
            else:  # nums[mid] == 2
                # Put 2 into the right zone.
                # Do not move mid yet: swapped-in value at mid is still unknown.
                self._swap(nums, mid, high)
                high -= 1

    @staticmethod
    def _swap(arr: List[int], from_index: int, to_index: int) -> None:
        arr[to_index], arr[from_index] = arr[from_index], arr[to_index]


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    solution = Solution()
    # your test code here
