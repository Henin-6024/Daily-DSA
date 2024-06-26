# 05 POTD 
# Problem: 237. Delete Node in a Linked List
# Language:  python3 
# Link: https://leetcode.com/problems/delete-node-in-a-linked-list/submissions/1250002031

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public void deleteNode(ListNode node) {
        node.val = node.next.val;
        node.next = node.next.next;
    }
}
