from typing import *
from leetcode.editor.common.node import *

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_head = ListNode(-1)
        dummy_head.next = head

        p1 = dummy_head
        p2 = dummy_head
        for _ in range(n + 1):
            p1 = p1.next

        # move p2 after p1 move n+1 nodes first. p2 will end up at node n + 1 before end to remove node n
        while p1 is not None:
            p1 = p1.next
            p2 = p2.next

        to_remove = p2.next
        p2.next = to_remove.next
        to_remove.next = None

        return dummy_head.next
        
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()
    # your test code here
    