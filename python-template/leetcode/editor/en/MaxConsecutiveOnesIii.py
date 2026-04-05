from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = right = 0  # [left, right)
        window_ones = max_len = 0
        while right < n:
            if nums[right] == 1:
                window_ones += 1
            right += 1
            while right - left - window_ones > k:
                if nums[left] == 1:
                    window_ones -= 1
                left += 1
            max_len = max(max_len, right - left)
        return max_len


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    solution = Solution()
    # your test code here
