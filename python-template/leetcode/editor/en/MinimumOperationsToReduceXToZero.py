from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # use a sliding window to find the longest subarray with sum sum(nums) - x
        n = len(nums)
        s = sum(nums)
        target = s - x

        left = right = 0  # [left, right)
        window_sum = 0
        max_len: int | None = None

        while right < n:
            window_sum += nums[right]
            right += 1

            while window_sum > target and left < right:
                window_sum -= nums[left]
                left += 1

            if window_sum == target:
                new_len = right - left
                if max_len is None:
                    max_len = new_len
                else:
                    max_len = max(max_len, new_len)

        return n - max_len if max_len is not None else -1


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    solution = Solution()
    # your test code here
