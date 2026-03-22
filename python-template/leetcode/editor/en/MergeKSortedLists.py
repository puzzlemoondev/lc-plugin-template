from typing import *
from leetcode.editor.common.node import *
import heapq

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        priority_queue = []
        for index, head in enumerate(lists):
            if head is not None:
                # index is needed in sorting to preserve insertion order
                heapq.heappush(priority_queue, (head.val, index, head))

        dummy_head = ListNode(-1)
        current = dummy_head
        while priority_queue:
            _, index, nxt = heapq.heappop(priority_queue)
            temp = nxt.next
            if temp is not None:
                heapq.heappush(priority_queue, (temp.val, index, temp))
            nxt.next = None
            current.next = nxt
            current = current.next

        return dummy_head.next



# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()
    # your test code here
    