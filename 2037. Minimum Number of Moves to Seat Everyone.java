/*
# 13 POTD 
# Problem: 2037. Minimum Number of Moves to Seat Everyone
# Language:  python3 
# Link: https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/submissions/1287336654
*/

class Solution {
  public int minMovesToSeat(int[] seats, int[] students) {
    int res = 0;

    Arrays.sort(seats);
    Arrays.sort(students);

    for (int i = 0; i < seats.length; ++i)
      res += Math.abs(seats[i] - students[i]);

    return res;
  }
}
