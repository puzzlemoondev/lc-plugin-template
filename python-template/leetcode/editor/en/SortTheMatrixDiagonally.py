from typing import *
from leetcode.editor.common.node import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        # find diagonals (x index and y index same diff)
        diagonals = self._find_diagonals(mat)
        for d in diagonals.values():
            d.sort(reverse=True)  # sort reverse because we will be popping from behind
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                diagonal_id = i - j
                diagonal = diagonals[diagonal_id]
                mat[i][j] = diagonal.pop()
        return mat

    @staticmethod
    def _find_diagonals(mat: List[List[int]]) -> dict[int, list[int]]:
        diagonals = {}
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                diagonal_id = i - j
                if diagonal_id not in diagonals:
                    diagonals[diagonal_id] = []
                diagonals[diagonal_id].append(mat[i][j])
        return diagonals


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    solution = Solution()
    # your test code here
