# author: YANG CUI
#  ID :   27346919

"""
Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    # def __str__(self):
    #     return str(self.val) + "->"

class Solution(object):
    def calculateLength(self, head):
        # returns the length of a given linkedlist in O(n)
        length = 0
        if head == None:
            return length
        else:
            current = head
            while current != None:
                length += 1
                current = current.next
        # print(length)
        return length

    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None or k == 0:
            return head
        else:
            act_len = self.calculateLength(head)
            abs_len = k % act_len
            ret_len = act_len - abs_len
            if act_len == 1 or abs_len == 0:
                return head
            front = head
            rear = head
            counter_front = 0
            counter_rear = 0
            if ret_len > 0:
                while counter_front < ret_len:
                    front = front.next
                    counter_front += 1

                while counter_rear < ret_len - 1:
                    rear = rear.next
                    counter_rear += 1
                temp = front
                while temp.next != None:
                    temp = temp.next
                temp.next = head
                rear.next = None
            return front

# L1 = ListNode(1)
# L1.next = ListNode(2)
# L1.next.next = ListNode(3)
# L1.next.next.next = ListNode(4)
# L1.next.next.next.next = ListNode(5)
# L1.next.next.next.next.next = None

# L2 = ListNode(1)
# L2.next = ListNode(2)
# L2.next.next = None

# L3 = ListNode(1)
# L3.next = None

# Sol = Solution()
# Sol.rotateRight(L3, 1)
