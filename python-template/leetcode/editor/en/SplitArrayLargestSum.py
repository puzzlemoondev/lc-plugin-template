from typing import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        return self.shipWithinDays(nums, k)

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = self.find_max_and_sum(weights)
        while left <= right:
            mid = left + (right - left) // 2
            days_needed_at_capacity = self.f(weights, mid)
            if (
                days_needed_at_capacity <= days
            ):  # capacity overshot, decrease right bound
                right = mid - 1
            else:  # insufficient capacity, increase left bound
                left = mid + 1
        return left

    @staticmethod
    def find_max_and_sum(weights: List[int]) -> Tuple[int, int]:
        m = 0
        s = 0
        for w in weights:
            m = max(m, w)
            s += w
        return m, s

    @staticmethod
    def f(weights: List[int], x: int) -> int:
        """
        x is ship capacity
        f(x) is the number of days needed to ship all weights
        f(x) shrinks as x grows
        constraint: sum(weights) >= x >= max(weights)
        """
        days = 0
        i = 0
        while i < len(weights):
            capacity = x
            while i < len(weights):
                if capacity < weights[i]:
                    break
                capacity -= weights[i]
                i += 1
            days += 1
        return days


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    solution = Solution()
    # your test code here
