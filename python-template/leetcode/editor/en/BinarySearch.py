from typing import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1  # [left, right]
        while (
            left <= right
        ):  # left <= right -> end condition is [right + 1, right]. this ensures every element is covered
            mid = (
                left + (right - left) // 2
            )  # do not (left + right) // 2, might overflow
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1  # mid already covered, search from right (mid + 1)
            elif nums[mid] > target:
                right = mid - 1  # mid already covered, search from left (mid - 1)
        return -1


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    solution = Solution()
    # your test code here
