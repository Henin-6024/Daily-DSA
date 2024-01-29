# 29 POTD 
# Problem: 232. Implement Queue using Stacks 
# Language :  python3
#link: https://leetcode.com/problems/implement-queue-using-stacks/submissions/1160204969?envType=daily-question&envId=2024-01-29

class MyQueue:

    def __init__(self):
        self.stack_in = []
        self.stack_out = []
        
    def push(self, x: int) -> None:
        self.stack_in.append(x)
        
    def pop(self) -> int:
        self.stack_shift()
        return self.stack_out.pop()

    def peek(self) -> int:
        self.stack_shift()
        return self.stack_out[-1]

    def empty(self) -> bool:
        return not self.stack_in and not self.stack_out

    def stack_shift(self):
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
