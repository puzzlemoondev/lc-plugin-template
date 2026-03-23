from typing import *
from leetcode.editor.common.node import *

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        # p1 points to head, p2 points to successor
        p1 = p2 = head
        for _ in range(k):
            if p2 is None:
                return head # no enough node, skip reverse
            p2 = p2.next
        new_head = self._reverseN(p1, k)
        # connect reversed
        p1.next = self.reverseKGroup(p2, k)
        return new_head

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


if __name__ == '__main__':
    solution = Solution()
    # your test code here
    