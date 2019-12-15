from typing import *

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        arithmetic = {'+', '-', '*', '/'}
        
        def do_math(first_op, second_op, op):
            res = 0
            print(str(first_op) + op + str(second_op))
            
            if op == '+':
                res = first_op + second_op
            elif op == '-':
                res = first_op - second_op
            elif op == '*':
                res = first_op * second_op
            else:
                res = int(first_op / second_op)
            
            return res
        
        for token in tokens:
            if token in arithmetic:
                first, second = stack.pop(), stack.pop()
                res = do_math(second, first, token)
                stack.append(res)
            else:
                stack.append(int(token))
        
        return stack.pop()
