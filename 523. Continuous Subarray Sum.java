/*
# 08 POTD 
# Problem: 523. Continuous Subarray Sum
# Language: Java
# Link https://leetcode.com/problems/continuous-subarray-sum/submissions/1281960222
*/

class Solution {
  public boolean checkSubarraySum(int[] nums, int k) {
    int prefix = 0;
    Map<Integer, Integer> prefixToIndex = new HashMap<>();
    prefixToIndex.put(0, -1);

    for (int i = 0; i < nums.length; ++i) {
      prefix += nums[i];
      if (k != 0)
        prefix %= k;
      if (prefixToIndex.containsKey(prefix)) {
        if (i - prefixToIndex.get(prefix) > 1)
          return true;
      } else {
        // Set a new key if it's absent because the previous index is better.
        prefixToIndex.put(prefix, i);
      }
    }

    return false;
  }
}
