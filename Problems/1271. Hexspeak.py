from typing import *

class Solution:
    def toHexspeak(self, num: str) -> str:
        num = int(num)
        res = ''
        map_ = {0:'O', 1:'I', 10:'A', 11:'B', 12:'C', 13:'D', 14: 'E', 15:'F'}
        
        while num > 0:
            rem = num % 16
            
            if not rem in map_:
                return "ERROR"
            
            res = map_[rem] + res
            num //= 16
        
        return res
