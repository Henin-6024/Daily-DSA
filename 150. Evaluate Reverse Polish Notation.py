# 30 POTD 
# Problem: 150. Evaluate Reverse Polish Notation
# Language :  python3 
# link: https://leetcode.com/problems/evaluate-reverse-polish-notation/submissions/1160640593?envType=daily-question&envId=2024-01-30

from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        no_stack = []
        for token in tokens:
            if len(token) > 1 or token.isdigit():
                no_stack.append(int(token))
            else:
                if token == '+':
                    no_stack[-2] += no_stack[-1]
                elif token == '-':
                    no_stack[-2] -= no_stack[-1]
                elif token == '*':
                    no_stack[-2] *= no_stack[-1]
                else:
                    no_stack[-2] = int(float(no_stack[-2]) / no_stack[-1])
                no_stack.pop()
        return no_stack[0]
