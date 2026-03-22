from typing import *
from leetcode.editor.common.node import *
from collections import deque

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1 = self._linked_list_to_stack(l1)
        s2 = self._linked_list_to_stack(l2)

        s = deque()

        carry = 0
        while s1 or s2 or carry:
            n = carry
            if s1:
                n += s1.pop()
            if s2:
                n += s2.pop()
            carry, digit = divmod(n, 10)
            s.append(digit)

        return self._stack_to_linked_list(s)

    @staticmethod
    def _linked_list_to_stack(ll: Optional[ListNode]) -> deque:
        stack = deque()
        current = ll
        while current:
            stack.append(current.val)
            current = current.next
        return stack

    @staticmethod
    def _stack_to_linked_list(stack: deque) -> Optional[ListNode]:
        if not stack:
            return None

        dummy = ListNode(-1)
        cur = dummy

        while stack:
            cur.next = ListNode(stack.pop())
            cur = cur.next

        return dummy.next




        
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()
    # your test code here
    