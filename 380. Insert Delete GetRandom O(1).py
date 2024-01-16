# 16th POTD 
# Problem: 380. Insert Delete GetRandom O(1) - LeetCode
# Language :  python 
#link: https://leetcode.com/problems/insert-delete-getrandom-o1/submissions/1147886474
class RandomizedSet:

    def __init__(self):
        self.index_dict = {}
        self.values_list = []

    def insert(self, val: int) -> bool:
        if val in self.index_dict:
            return False
        self.index_dict[val] = len(self.values_list)
        self.values_list.append(val)
        return True
        
    def remove(self, val: int) -> bool:
        if val not in self.index_dict:
            return False
        index_to_remove = self.index_dict[val]
        last_element = self.values_list[-1]
        self.values_list[index_to_remove] = last_element
        self.index_dict[last_element] = index_to_remove
        self.values_list.pop()
        del self.index_dict[val]
        return True

    def getRandom(self) -> int:
        return choice(self.values_list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
