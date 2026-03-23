from typing import *
from leetcode.editor.common.node import *

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # reverse k group special case
        if not head or not head.next:
            return head
        # p1 points to head, p2 points to successor
        p1 = p2 = head
        for _ in range(2):
            if p2 is None:
                return head # no enough node, skip reverse
            p2 = p2.next
        new_head = self._swap(p1)
        # connect reversed
        p1.next = self.swapPairs(p2)
        return new_head

    @staticmethod
    def _swap(head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        pre, cur, nxt = None, head, head.next
        for _ in range(2):
            cur.next = pre
            pre = cur
            cur = nxt
            if nxt:
                nxt = nxt.next
        head.next = cur
        return pre
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()
    # your test code here
    