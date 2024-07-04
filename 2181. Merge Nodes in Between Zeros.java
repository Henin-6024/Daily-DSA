/**
# 04 POTD 
# Problem: 2181. Merge Nodes in Between Zeros
# Language : Java
# Link: https://leetcode.com/problems/merge-nodes-in-between-zeros/submissions/1309686632


 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
  public ListNode mergeNodes(ListNode head) {
    if (head == null)
      return null;
    if (head.next.val == 0) {
      ListNode node = new ListNode(head.val);
      node.next = mergeNodes(head.next.next);
      return node;
    }

    ListNode next = mergeNodes(head.next);
    next.val += head.val;
    return next;
  }
}
