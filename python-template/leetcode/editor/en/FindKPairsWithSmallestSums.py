from typing import *
from leetcode.editor.common.node import *
import heapq


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        pq = []
        for i, n in enumerate(nums1):
            heapq.heappush(pq, (n + nums2[0], i, 0))
        len_nums2 = len(nums2)
        pairs = []
        while pq:
            s, i, j = heapq.heappop(pq)
            pairs.append([nums1[i], nums2[j]])
            if len(pairs) == k:
                break
            j_nxt = j + 1
            if j_nxt < len_nums2:
                heapq.heappush(pq, (nums1[i] + nums2[j_nxt], i, j_nxt))

        return pairs


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    solution = Solution()
    # your test code here
