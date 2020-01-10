from typing import *

class Solution:
    def intToRoman(self, num: int) -> str:
        denoms = {
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I',
        }
        
        ans = []
        
        for divider, denom in denoms.items():
            res = num // divider
            
            if res:
                ans.append(denom*res)
                num = num % divider
        
        return ''.join(ans)
