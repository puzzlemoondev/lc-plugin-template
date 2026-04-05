from typing import Optional
from leetcode.editor.common.node import ListNode


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        lt_dummy_head = ListNode(-1)
        lt = lt_dummy_head
        gt_dummy_head = ListNode(-1)
        gte = gt_dummy_head

        current = head
        while current:
            nxt = current.next
            current.next = None
            if current.val < x:
                lt.next = current
                lt = lt.next
            else:
                gte.next = current
                gte = gte.next
            current = nxt

        lt.next = gt_dummy_head.next
        return lt_dummy_head.next


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    solution = Solution()
    # your test code here
