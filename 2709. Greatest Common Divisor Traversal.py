# 25 POTD 
# Problem: 2709. Greatest Common Divisor Traversal
# Language :  python3
# Link: https://leetcode.com/problems/greatest-common-divisor-traversal/submissions/1185744513

class UnionFind:
    def __init__(self, size):
        self.parents = list(range(size))
        self.sizes = [1] * size

    def find(self, node):
        if self.parents[node] != node:
            self.parents[node] = self.find(self.parents[node])
        return self.parents[node]

    def union(self, node_a, node_b):
        root_a, root_b = self.find(node_a), self.find(node_b)
        if root_a == root_b:
            return False 
      
        if self.sizes[root_a] > self.sizes[root_b]:
            self.parents[root_b] = root_a
            self.sizes[root_a] += self.sizes[root_b]
        else:
            self.parents[root_a] = root_b
            self.sizes[root_b] += self.sizes[root_a]
        return True


max_value = 100010

prime_factors = defaultdict(list)

for number in range(1, max_value + 1):
    value = number
    factor = 2
    while factor <= value // factor:
        if value % factor == 0:
            prime_factors[number].append(factor)
            while value % factor == 0:
                value //= factor
        factor += 1
    if value > 1:
        prime_factors[number].append(value)

class Solution:
    def canTraverseAllPairs(self, nums):
        count = len(nums)
        max_num = max(nums)
      
        uf = UnionFind(count + max_num + 1)
        for i, num in enumerate(nums):
            for prime in prime_factors[num]:
                uf.union(i, prime + count)
              
        root_set = {uf.find(i) for i in range(count)}
        return len(root_set) == 1
