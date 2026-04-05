from typing import *
from leetcode.editor.common.node import *

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        # find lengths of each list
        len_a = self._find_list_length(headA)
        len_b = self._find_list_length(headB)

        # advance longer list n steps to make the start equal
        if len_a > len_b:
            headA = self._advance_steps(headA, len_a - len_b)
        elif len_b > len_a:
            headB = self._advance_steps(headB, len_b - len_a)

        # advance both list and return intersection if exists, since there's no cycle we can safely use while loop to advance
        while headA and headB:
            if headA is headB:
                return headA
            headA = headA.next
            headB = headB.next

        return None

    @staticmethod
    def _find_list_length(head: ListNode) -> int:
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        return length

    @staticmethod
    def _advance_steps(head: ListNode, steps: int) -> Optional[ListNode]:
        end = head
        for _ in range(steps):
            if not end.next:
                return None
            end = end.next
        return end


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    solution = Solution()
    # your test code here
