# 07 POTD 
# Problem: 876. Middle of the Linked List
# Language :  python3 
# Link: https://leetcode.com/problems/middle-of-the-linked-list/submissions/1196330137?envType=daily-question&envId=2024-03-07

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow_pointer = fast_pointer = head
        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
        return slow_pointer
