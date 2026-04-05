from typing import *
from leetcode.editor.common.node import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])

        ans = self._zeros(n, m)
        for i in range(m):
            for j in range(n):
                ans[j][i] = matrix[i][j]

        return ans

    @staticmethod
    def _zeros(m: int, n: int) -> List[List[int]]:
        return [[0] * n for _ in range(m)]


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    solution = Solution()
    # your test code here
