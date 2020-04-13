from typing import *

class Solution:
    def reverseWords(self, s: str) -> str:
        left = None
        n = len(s)
        arr = list(s)
        
        def mirror(left, right):
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
        
        for i in range(n):
            if s[i] == ' ':
                if left is not None:
                    mirror(left, i-1)
                    left = None
            elif left is None:
                left = i
            elif i == n-1:
                if left is not None:
                    mirror(left, n-1)
        
        return ''.join(arr)

s = Solution()

s.reverseWords("Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc"