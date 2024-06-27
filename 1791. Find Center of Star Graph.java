# 27 POTD 
# Problem: 1791. Find Center of Star Graph
# Language : Java
# Link: https://leetcode.com/problems/find-center-of-star-graph/submissions/1302109999
class Solution {
    public int findCenter(int[][] edges) {
        return edges[0][0] == edges[1][0] || edges[0][0] == edges[1][1]
            ? edges[0][0]
            : edges[0][1];    
    }
}
