from typing import *
from leetcode.editor.common.node import *

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        if not head.next:
            return True
        mid = self._find_mid(head)
        left, right = head, self._reverse(mid)
        while right:
            if right.val != left.val:
                return False
            right = right.next
            left = left.next
        return True

    @staticmethod
    def _find_mid(head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

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

        
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()
    # your test code here
    