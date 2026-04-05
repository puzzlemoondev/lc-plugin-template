from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class NumArray:
    def __init__(self, nums: List[int]):
        self.pre_sum = self._calculate_pre_sum(nums)

    def sumRange(self, left: int, right: int) -> int:
        return self.pre_sum[right + 1] - self.pre_sum[left]

    @staticmethod
    def _calculate_pre_sum(nums: List[int]) -> List[int]:
        n = len(nums)
        pre_sum: List[int] = [0] * (n + 1)
        for i in range(1, n + 1):
            pre_sum[i] = pre_sum[i - 1] + nums[i - 1]
        return pre_sum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    solution = NumArray([1, 2])
    # your test code here
    print(solution.pre_sum)
