from typing import *
from leetcode.editor.common.node import *

import heapq

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # variation of merging k sorted linked list

        arr_len = len(matrix[0])

        pq = []
        for idx, arr in enumerate(matrix):
            heapq.heappush(pq, (arr[0], idx, 0))

        n = 1
        while pq:
            val, idx_arr, idx_item = heapq.heappop(pq)
            if n == k:
                return val
            idx_nxt = idx_item + 1
            if idx_nxt < arr_len:
                nxt = matrix[idx_arr][idx_nxt]
                heapq.heappush(pq, (nxt, idx_arr, idx_nxt))
            n += 1

        raise RuntimeError('no solution')

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()
    # your test code here
    