from typing import *

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        queue = []
        m = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        buttons = m.keys()
        digits = list(digits)
        filtered_digits = list(filter(lambda x: x in buttons, digits))
        
        if len(filtered_digits) == 0:
            return queue
    
        queue = [letter for letter in m[filtered_digits.pop(0)]]
        
        for digit in filtered_digits:
            size = len(queue)
            
            for _ in range(size):
                val = queue.pop(0)
                
                for letter in m[digit]:
                    new_val = val + letter
                    queue.append(new_val)
            
        return queue

s = Solution()
assert s.letterCombinations("23") == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
assert s.letterCombinations("01*#") == []
assert s.letterCombinations("") == []