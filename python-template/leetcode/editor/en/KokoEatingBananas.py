from typing import *
from leetcode.editor.common.node import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, pow(10, 9)  # question constraint
        while left <= right:
            mid = left + (right - left) // 2
            # find left bound
            if self.f(piles, mid) <= h:
                # need to make f(x) bigger (x smaller)
                right = mid - 1
            else:
                left = mid + 1
        return left

    @staticmethod
    def f(piles: List[int], x: int) -> int:
        """
        x is speed (bananas per hour)
        f(x) is hours needed to eat all piles
        f(x) shrinks as x grows
        """
        hrs = 0
        for pile in piles:
            hr, remaining = divmod(pile, x)
            hrs += hr
            if remaining:
                hrs += 1
        return hrs


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    solution = Solution()
    # your test code here
