from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        return self.nSum(nums, 4, 0, target)

    def nSum(self, nums: List[int], n: int, start: int, target: int) -> List[List[int]]:
        ans: List[List[int]] = []
        size = len(nums)

        if n < 2 or size < n:
            return ans

        if n == 2:
            ans.extend(self.twoSum(nums, start, target))
            return ans

        i = start
        while i < size:
            sums = self.nSum(nums, n - 1, i + 1, target - nums[i])
            for s in sums:
                s.append(nums[i])
                ans.append(s)
            i = self._move_left_pointer(nums, i)

        return ans

    def twoSum(self, nums: list[int], start: int, target: int) -> list[list[int]]:
        ans: list[list[int]] = []
        left, right = start, len(nums) - 1
        while left < right:
            s = nums[left] + nums[right]
            if s == target:
                ans.append([nums[left], nums[right]])
                left = self._move_left_pointer(nums, left)
                right = self._move_right_pointer(nums, right)
            elif s < target:
                left = self._move_left_pointer(nums, left)
            else:
                right = self._move_right_pointer(nums, right)
        return ans

    def _move_left_pointer(self, nums: list[int], left: int) -> int:
        return left + (self._steps_to_different_item(nums, left) or 1)

    def _move_right_pointer(self, nums: list[int], right: int) -> int:
        return right - (self._steps_to_different_item(nums, right, step=-1) or 1)

    @staticmethod
    def _steps_to_different_item(nums: list[int], index: int, step=1) -> int:
        val = nums[index]
        current_index = index
        while val == nums[current_index]:
            next_index = current_index + 1
            if next_index == len(nums):
                break
            current_index += step
        return (current_index - index) * step
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()
    # your test code here
    print(solution.fourSum([1,0,-1,0,-2,2], 0))
    