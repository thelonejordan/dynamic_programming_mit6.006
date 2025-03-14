from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def from_list(l: List[int]):
        if len(l) == 0: raise RuntimeError("invalid arg")
        if len(l) == 1 and l[0] == 0: return ListNode()
        head = None
        for item in reversed(l):
            head = ListNode(item, head)
        return head

    def to_list(self) -> List[int]:
        cur = self
        digits = []
        while cur:
            digits.append(cur.val)
            cur = cur.next
        return digits

def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
    carried = 0
    digits = []
    while True:
        val = carried
        if l1:
            val += l1.val
            l1 = l1.next
        if l2:
            val += l2.val
            l2 = l2.next
        val, carried = val % 10, val // 10
        if val == 0 and carried == 0 and len(digits) > 0:
            break
        digits.append(val)
    return ListNode.from_list(digits)

if __name__ == "__main__":
    # l1 = [2,4,3]
    # l2 = [5,6,4]
    l1 = [9,9,9,9,9,9,9]
    l2 = [9,9,9,9]
    nl1 = ListNode.from_list(l1)
    nl2 = ListNode.from_list(l2)
    # assert nl1.val == 2
    # assert nl1.next.val == 4
    # assert nl1.next.next.val == 3
    # assert nl1.next.next.next is None
    # assert nl2.val == 5
    # assert nl2.next.val == 6
    # assert nl2.next.next.val == 4
    # assert nl2.next.next.next is None
    # assert tuple(l1) == tuple(nl1.to_list())
    # assert tuple(l2) == tuple(nl2.to_list())
    nl3 = addTwoNumbers(nl1, nl2)
    print(nl3.to_list())
    # print(l3.to_list())
