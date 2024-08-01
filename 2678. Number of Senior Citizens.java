/*
# 01 POTD 
# Problem: 2678. Number of Senior Citizens
# Language: Java 
# Link: https://leetcode.com/problems/number-of-senior-citizens/submissions/1341023002
*/
class Solution {
  public int countSeniors(String[] details) {
    return (int) Arrays.stream(details)
        .filter(detail -> Integer.parseInt(detail.substring(11, 13)) > 60)
        .count();
  }
}
