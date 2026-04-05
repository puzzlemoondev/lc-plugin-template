from typing import *
from leetcode.editor.common.node import *


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        # 0. find length
        n = self._length(head)
        k = k % n
        if k == 0:
            return head
        # 1. reverse full list
        head = self._reverse(head)
        # 2. reverse first k nodes
        head = self._reverse_n(head, k)
        # 3. reverse remaining nodes
        pre = head
        for _ in range(1, k):
            pre = pre.next
        pre.next = self._reverse(pre.next)
        return head

    @staticmethod
    def _length(head: Optional[ListNode]) -> int:
        length = 0
        while head:
            length += 1
            head = head.next
        return length

    @staticmethod
    def _reverse(head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        pre, cur, nxt = None, head, head.next
        while cur:
            cur.next = pre
            pre = cur
            cur = nxt
            if nxt:
                nxt = nxt.next
        return pre

    @staticmethod
    def _reverse_n(head: Optional[ListNode], n: int) -> Optional[ListNode]:
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
        head.next = cur
        return pre


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    solution = Solution()
    # your test code here
