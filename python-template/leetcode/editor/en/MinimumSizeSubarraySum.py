from typing import *

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = right = 0
        window_sum = 0
        min_len: int | None = None
        while right < len(nums):
            window_sum += nums[right]
            right += 1
            while left < right and window_sum >= target:
                if window_sum >= target:
                    new_len = right - left
                    min_len = new_len if min_len is None else min(min_len, new_len)
                window_sum -= nums[left]
                left += 1
        return min_len or 0
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()
    # your test code here
    