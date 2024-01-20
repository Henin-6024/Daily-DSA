# 17 POTD 
# Problem: 
# Language : 907. Sum of Subarray Minimums
# link: https://leetcode.com/problems/sum-of-subarray-minimums/submissions/1151206231?envType=daily-question&envId=2024-01-20

class Solution:
    def sumSubarrayMins(self, arr):
        kMod = 10 ** 9 + 7
        n = len(arr)
        left, right = [1] * n, [1] * n
        def fillLength(counts, start, end, step):      
            s = []
            for i in range(start, end, step):        
                num = arr[i] if step > 0 else arr[i] - 1        
                while s and s[-1][0] > num:
                    counts[i] += s.pop()[1]
                s.append((arr[i], counts[i]))
        fillLength(left, 0, n, 1)
        fillLength(right, n - 1, -1, -1)
        result = sum(a * l * r for a, l, r in zip(arr, left, right)) % kMod
        return result
