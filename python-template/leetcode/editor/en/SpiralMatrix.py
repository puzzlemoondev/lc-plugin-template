from typing import *
from leetcode.editor.common.node import *

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        x, y = self._shape(matrix)
        upper_bound = left_bound = 0
        lower_bound = y - 1
        right_bound = x - 1
        ans = []
        while len(ans) < x * y:
            # top left to right
            if upper_bound <= lower_bound:
                for idx_x in range(left_bound, right_bound + 1):
                    ans.append(matrix[upper_bound][idx_x])
                upper_bound += 1
            # right top to bottom
            if right_bound >= left_bound:
                for idx_y in range(upper_bound, lower_bound + 1):
                    ans.append(matrix[idx_y][right_bound])
                right_bound -= 1
            # bottom right to left
            if lower_bound >= upper_bound:
                for idx_x in reversed(range(left_bound, right_bound + 1)):
                    ans.append(matrix[lower_bound][idx_x])
                lower_bound -= 1
            # left bottom to top
            if left_bound <= right_bound:
                for idx_y in reversed(range(upper_bound, lower_bound + 1)):
                    ans.append(matrix[idx_y][left_bound])
                left_bound += 1
        return ans

    @staticmethod
    def _shape(matrix: List[List[int]]) -> Tuple[int, int]:
        return len(matrix[0]), len(matrix)
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()
    # your test code here
    