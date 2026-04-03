from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = right = 0
        current_product = 1
        res = 0
        while right < n:
            current_product *= nums[right]
            right += 1
            while left < right and current_product >= k:
                current_product /= nums[left]
                left += 1
            res += right - left
        return res
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()
    # your test code here
    