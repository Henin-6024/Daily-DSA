/*
# 30 POTD 
# Problem: 1442. Count Triplets That Can Form Two Arrays of Equal XOR
# Language :  Java
# Link: https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/submissions/1272470118
*/
class Solution {
    public int countTriplets(int[] arr) {
    int length = arr.length;
    int [] prefixXOR = new int[length + 1];
    for (int i = 0; i< length; ++i) {
        prefixXOR[i + 1] = prefixXOR[i] ^ arr[i];
    }    
    int count = 0;
    for (int i = 0; i < length - 1; ++i) {
        for(int j = i + 1; j < length; ++j) {
            for (int k = j; k < length; ++k) {
                int xorA = prefixXOR[j] ^ prefixXOR[i];
                int xorB = prefixXOR[k + 1] ^ prefixXOR[j];
                if (xorA == xorB) {
                    count++;
                }  
            }
        }
    }
    return count;
    }
}
