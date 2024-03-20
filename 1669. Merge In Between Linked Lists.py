# 20 POTD 
# Problem: 1669. Merge In Between Linked Lists
# Language :  python3 
# Link: https://leetcode.com/problems/merge-in-between-linked-lists/submissions/1209173167

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        node_before_a = list1
        for i in range(a - 1):
            node_before_a = node_before_a.next
        node_b = node_before_a.next
        for i in range(b - a):
            node_b = node_b.next
        node_before_a.next = list2
        last_node_inlist2 = list2
        while last_node_inlist2.next:
            last_node_inlist2 = last_node_inlist2.next
        last_node_inlist2.next = node_b.next
        node_b.next = None
        return list1

