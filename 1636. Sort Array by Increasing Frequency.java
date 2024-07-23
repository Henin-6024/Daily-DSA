/*
# 23 POTD 
# Problem: 1636. Sort Array by Increasing Frequency
# Language : Java 
# Link: https://leetcode.com/problems/sort-array-by-increasing-frequency/submissions/1330891614
*/
class T {
  public int num;
  public int freq;
  public T(int num, int freq) {
    this.num = num;
    this.freq = freq;
  }
};
 
class Solution {
  public int[] frequencySort(int[] nums) {
    int[] ans = new int[nums.length];
    int ansIndex = 0;
    Map<Integer, Integer> count = new HashMap<>();
    Queue<T> heap =
        new PriorityQueue<>((a, b) -> a.freq == b.freq ? b.num - a.num : a.freq - b.freq);

    for (final int num : nums)
      count.merge(num, 1, Integer::sum);

    for (Map.Entry<Integer, Integer> entry : count.entrySet())
      heap.offer(new T(entry.getKey(), entry.getValue()));

    while (!heap.isEmpty()) {
      final int num = heap.peek().num;
      final int freq = heap.poll().freq;
      for (int i = 0; i < freq; ++i)
        ans[ansIndex++] = num;
    }

    return ans;
  }
}
