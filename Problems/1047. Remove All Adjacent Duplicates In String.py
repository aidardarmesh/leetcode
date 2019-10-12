from typing import *

class Solution:
    def removeDuplicates(self, S: str) -> str:
        has_duplicates = True
        queue = list(S)

        while has_duplicates:
            temp = []
            has_duplicates = False

            while len(queue) > 1:
                ch = queue.pop(0)
                
                if ch == queue[0]:
                    queue.pop(0)
                    has_duplicates = True
                else:
                    temp.append(ch)
            
            temp += queue
            queue = temp

        return "".join(queue)

s = Solution()

assert s.removeDuplicates("abbaca") == "ca"