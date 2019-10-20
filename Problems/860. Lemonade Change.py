from typing import *

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = {}

        while bills:
            bill = bills.pop(0)

            if bill == 5:
                change[5] = change.get(5, 0) + 1
            elif bill == 10:
                changes_5 = change.get(5, 0)

                if changes_5:
                    change[5] -= 1
                    change[10] = change.get(10, 0) + 1
                else:
                    return False
            elif bill == 20:
                changes_10 = change.get(10, 0)
                changes_5 = change.get(5, 0)

                if changes_10 and changes_5:
                    change[10] -= 1
                    change[5] -= 1
                elif changes_5 >= 3:
                    change[5] -= 3
                else:
                    return False
                
                change[20] = change.get(20, 0) + 1
        
        return True

s = Solution()

assert s.lemonadeChange([5,5,5,10,20]) == True
assert s.lemonadeChange([5,5,10]) == True
assert s.lemonadeChange([10,10]) == False
assert s.lemonadeChange([5,5,10,10,20]) == False