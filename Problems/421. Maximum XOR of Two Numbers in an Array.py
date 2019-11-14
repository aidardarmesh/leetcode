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

        max_xor = 0

        for num in nums:
            node_xor = trie
            curr_xor = 0
            for bit in num:
                opp_bit = 1 - bit
                if opp_bit in node_xor:
                    curr_xor = (curr_xor << 1) | 1
                    node_xor = node_xor[opp_bit]
                else:
                    curr_xor = curr_xor << 1
                    node_xor = node_xor[bit]
        
            max_xor = max(max_xor, curr_xor)

        return max_xor

s = Solution()

assert s.findMaximumXOR([3, 10, 5, 25, 2, 8]) == 28