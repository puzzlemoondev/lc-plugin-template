from typing import *
from leetcode.editor.common.node import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # clock-wise rotate = transpose + reverse
        # anti-clock-wise rotate = reverse + transpose
        self._transpose(matrix)
        self._reverse(matrix)

    @staticmethod
    def _transpose(matrix: List[List[int]]) -> None:
        shape = len(matrix)
        for x in range(shape):
            for y in range(
                x, shape
            ):  # y > x (lower triangle only to avoid swapping twice)
                matrix[x][y], matrix[y][x] = matrix[y][x], matrix[x][y]

    @staticmethod
    def _reverse(matrix: List[List[int]]) -> None:
        shape = len(matrix)
        for row in matrix:
            left, right = 0, shape - 1
            while left < right:
                row[left], row[right] = row[right], row[left]
                left += 1
                right -= 1


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    solution = Solution()
    # your test code here
