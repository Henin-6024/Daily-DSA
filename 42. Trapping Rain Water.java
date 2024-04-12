# 12 POTD 
# Problem: 42. Trapping Rain Water
# Language:  JAVA 
# Link: https://leetcode.com/problems/trapping-rain-water/submissions/1230024853


class Solution {
    public int trap(int[] height) {
        if(height.length == 0) return 0;
        int ans = 0;
        int l = 0;
        int r = height.length - 1;
        int maxL = height[l];
        int maxR = height[r];
        while(l<r)
            if (maxL < maxR){
                ans += maxL - height[l];
                maxL = Math.max(maxL,height[++l]);
            }else{
                ans += maxR- height[r];
                maxR = Math.max(maxR, height[--r]);
            }
        return ans;
    }
    
}
