from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.leftBound(nums, target)
        if left != -1:
            right = self.rightBound(nums[left:], target)
            if right != -1:
                return [left, left + right]
        return [-1, -1]

    @staticmethod
    def leftBound(nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] == target:
                right = mid - 1 # decrease right bound
        if left < 0 or left >= len(nums):
            return -1
        return left if nums[left] == target else -1

    @staticmethod
    def rightBound(nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] == target:
                left = mid + 1 # increase left bound
        if right < 0 or right >= len(nums):
            return -1
        return right if nums[right] == target else -1
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()
    # your test code here
    