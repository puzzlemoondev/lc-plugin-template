from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.pre_sum = self._calculate_pre_sum(matrix)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # calculate full region
        full = self.pre_sum[row2 + 1][col2 + 1]
        # calculate sub-regions
        # 1. calculate upper left corner
        # 2. calculate upper
        # 3. calculate left
        upper_left = self.pre_sum[row1][col1]
        upper = self.pre_sum[row2 + 1][col1]
        left = self.pre_sum[row1][col2 + 1]
        # full - upper - left + upper left = answer
        return full - upper - left + upper_left

    @staticmethod
    def _calculate_pre_sum(matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        if m == 0 or n == 0:
            return []
        pre_sum = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                pre_sum[i][j] = (
                        pre_sum[i - 1][j]
                        + pre_sum[i][j - 1]
                        + matrix[i - 1][j - 1]
                        - pre_sum[i - 1][j - 1]
                )
        return pre_sum

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        nums = NumMatrix(mat)
        m,n = len(mat), len(mat[0])
        res = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                row1, col1 = max(0, i - k), max(0, j - k)
                row2, col2 = min(m - 1, i + k), min(n - 1, j + k)
                res[i][j] = nums.sumRegion(row1, col1, row2, col2)
        return res
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()
    # your test code here
    solution.matrixBlockSum([
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ], 1)
    