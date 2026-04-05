from typing import *
from leetcode.editor.common.node import *


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # variation of linked list partition problem. create two partitions first
        dummy_uniq = ListNode(101)
        dummy_dup = ListNode(102)

        current_uniq = dummy_uniq
        current_dup = dummy_dup
        current = head
        while current:
            if current.val == current_dup.val or (
                current.next and current.val == current.next.val
            ):
                current_dup.next = current
                current_dup = current_dup.next
            else:
                current_uniq.next = current
                current_uniq = current_uniq.next
            current = current.next
            current_dup.next = None
            current_uniq.next = None

        return dummy_uniq.next


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    solution = Solution()
    # your test code here
