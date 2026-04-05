from typing import List
from sortedcontainers import SortedList


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def containsNearbyAlmostDuplicate(
        self, nums: List[int], indexDiff: int, valueDiff: int
    ) -> bool:
        left = right = 0
        window = SortedList()
        while right < len(nums):
            # abs(nums[left] - nums[right]) <= valueDiff equals to
            # nums[right] - valueDiff <= nums[left] <= nums[right] + valueDiff
            lower_bound = nums[right] - valueDiff
            upper_bound = nums[right] + valueDiff
            # find the closest value to lower_bound in the sorted window
            idx = window.bisect_left(lower_bound)
            # idx < len(window): guard out-of-bounds
            num: int | None = None
            if idx < len(window):
                num = window[idx]
            # check num within upper_bound
            if num is not None and num <= upper_bound:
                return True
            window.add(nums[right])
            right += 1
            while right - left > indexDiff:
                window.remove(nums[left])
                left += 1
        return False


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    solution = Solution()
    # your test code here
