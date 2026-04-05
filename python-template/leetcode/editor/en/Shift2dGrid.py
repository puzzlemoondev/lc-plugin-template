from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        mn = m * n
        k = k % mn
        # reverse 0 ~ mn - k - 1
        self._reverse_1d(grid, 0, mn - k - 1)
        # reverse mn - k ~ mn - 1
        self._reverse_1d(grid, mn - k, mn - 1)
        # reverse full
        self._reverse_1d(grid, 0, mn - 1)
        return grid

    def _reverse_1d(self, grid: List[List[int]], index_1: int, index_2: int) -> None:
        while index_1 < index_2:
            self._swap_1d(grid, index_1, index_2)
            index_1 += 1
            index_2 -= 1

    def _swap_1d(self, grid: List[List[int]], index_1: int, index_2: int) -> None:
        val_1 = self._get_1d(grid, index_1)
        val_2 = self._get_1d(grid, index_2)
        self._set_1d(grid, index_1, val_2)
        self._set_1d(grid, index_2, val_1)

    def _get_1d(self, grid: List[List[int]], index: int) -> int:
        i, j = self._translate_1d(grid, index)
        return grid[i][j]

    def _set_1d(self, grid: List[List[int]], index: int, value: int) -> None:
        i, j = self._translate_1d(grid, index)
        grid[i][j] = value

    @staticmethod
    def _translate_1d(grid: List[List[int]], index: int) -> tuple[int, int]:
        n = len(grid[0])
        return divmod(index, n)


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    solution = Solution()
    # your test code here
