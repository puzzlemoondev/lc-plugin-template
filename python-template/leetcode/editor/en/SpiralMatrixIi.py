from typing import *
from leetcode.editor.common.node import *

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = self._zeros(n)
        upper_bound = left_bound = 0
        right_bound = lower_bound = n - 1
        num = 1
        while num <= n * n:
            # top left to right
            if upper_bound <= lower_bound:
                for idx_x in range(left_bound, right_bound + 1):
                    ans[upper_bound][idx_x] = num
                    num += 1
                upper_bound += 1
            # right top to bottom
            if right_bound >= left_bound:
                for idx_y in range(upper_bound, lower_bound + 1):
                    ans[idx_y][right_bound] = num
                    num += 1
                right_bound -= 1
            # bottom left to right
            if lower_bound >= upper_bound:
                for idx_x in reversed(range(left_bound, right_bound + 1)):
                    ans[lower_bound][idx_x] = num
                    num += 1
                lower_bound -= 1
            # left bottom to top
            if left_bound <= right_bound:
                for idx_y in reversed(range(upper_bound, lower_bound + 1)):
                    ans[idx_y][left_bound] = num
                    num += 1
                left_bound += 1
        return ans

    @staticmethod
    def _zeros(n: int) -> List[List[int]]:
        return [[0 for _ in range(n)] for _ in range(n)]
        
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()
    # your test code here
    print(solution.generateMatrix(1))
    