from typing import *


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        # maximum length of larget number in binary repr
        L = len(bin(max(nums)))-2

        # convering all nums to bin list in bin form
        nums = [[(num >> i) & 1 for i in range(L)][::-1] for num in nums]

        # inserting all nums to common trie
        trie = {}
        for num in nums:
            node = trie
            for bit in num:
                if not bit in node:
                    node[bit] = {}
                node = node[bit]



s = Solution()

assert s.findMaximumXOR([3, 10, 5, 25, 2, 8]) == 28