class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        num = 0
        J = set(J) # O(1)
        
        for ch in S:
            if ch in J:
                num += 1
        
        return num

s = Solution()
print(s.numJewelsInStones("aA", "aAAbbbb"))

print(s.numJewelsInStones("z", "ZZ"))