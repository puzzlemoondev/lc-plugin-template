from typing import *
from leetcode.editor.common.node import *


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        if left == 1:
            return self._reverseN(head, right)
        pre = head
        # advance pre to node left - 1
        for _ in range(1, left - 1):
            pre = pre.next
        # reverse node
        pre.next = self._reverseN(pre.next, right - left + 1)
        return head

    @staticmethod
    def _reverseN(head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        pre, cur, nxt = None, head, head.next
        while n > 0:
            cur.next = pre
            pre = cur
            cur = nxt
            if nxt:
                nxt = nxt.next
            n -= 1
        # after while loop cur is at node n + 1 (successor), connect last (old head) to successor
        head.next = cur
        # pre is at node n (new head)
        return pre


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    solution = Solution()
    # your test code here
