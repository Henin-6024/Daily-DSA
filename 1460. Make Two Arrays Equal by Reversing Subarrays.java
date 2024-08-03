/*
# 03 POTD 
# Language :  Java
# Problem: 1460. Make Two Arrays Equal by Reversing Subarrays
# Link: https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/submissions/1343380403
*/
class Solution {
  public boolean canBeEqual(int[] target, int[] arr) {
    return Arrays.stream(arr)
        .boxed()
        .collect(Collectors.groupingBy(Integer::intValue, Collectors.counting()))
        .equals(Arrays.stream(target).boxed().collect(
            Collectors.groupingBy(Integer::intValue, Collectors.counting())));
  }
}
