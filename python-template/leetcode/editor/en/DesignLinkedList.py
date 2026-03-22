from typing import Self


# leetcode submit region begin(Prohibit modification and deletion)
class MyLinkedList:
    class Node:
        def __init__(self, val: int):
            self.val = val
            self.prev: Self | None = None
            self.next: Self | None = None

    def __init__(self):
        self._head = MyLinkedList.Node(0)
        self._tail = MyLinkedList.Node(0)
        self._head.next = self._tail
        self._tail.prev = self._head
        self._size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self._size:
            return -1
        return self._get_node(index).val

    def addAtHead(self, val: int) -> None:
        self._add_between(val, self._head, self._head.next)

    def addAtTail(self, val: int) -> None:
        self._add_between(val, self._tail.prev, self._tail)

    def addAtIndex(self, index: int, val: int) -> None:
        if index <= 0:
            self.addAtHead(val)
            return
        if index == self._size:
            self.addAtTail(val)
            return
        if index > self._size:
            return
        node = self._get_node(index)
        self._add_between(val, node.prev, node)

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self._size:
            return
        node = self._get_node(index)
        node.prev.next = node.next
        node.next.prev = node.prev
        self._size -= 1

    def _add_between(
        self, val: int, prev_node: MyLinkedList.Node, next_node: MyLinkedList.Node
    ) -> None:
        node = MyLinkedList.Node(val)
        prev_node.next = node
        node.prev = prev_node
        node.next = next_node
        next_node.prev = node
        self._size += 1

    def _get_node(self, index: int):
        p = self._head.next
        for _ in range(index):
            p = p.next
        return p


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    solution = Solution()
    # your test code here
