/*
# 22 POTD 
# Problem: 100. Same Tree
# Language :  python3 
# Link: https://leetcode.com/problems/sort-the-people/submissions/1329710912
*/
class Solution {
  public String[] sortPeople(String[] names, int[] heights) {
    List<Pair<Integer, String>> heightAndNames = new ArrayList<>();

    for (int i = 0; i < names.length; ++i)
      heightAndNames.add(new Pair<>(heights[i], names[i]));

    Collections.sort(heightAndNames, (a, b) -> b.getKey() - a.getKey());

    for (int i = 0; i < heightAndNames.size(); ++i)
      names[i] = heightAndNames.get(i).getValue();

    return names;
  }
}
