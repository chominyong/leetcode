# 2. Add Two Numbers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        digit = 1
        output = 0
        while l1 != None or l2 != None:
            if l1 != None:
                output += digit * l1.val
                l1 = l1.next
            if l2 != None:
                output += digit * l2.val
                l2 = l2.next
            digit *= 10

        str_digit = str(output)
        prev = ListNode(str_digit[0])
        for i in range(1, len(str_digit)):
            final = ListNode(str_digit[i])
            final.next = prev
            prev = final
        try:
            return final
        except:
            return prev
