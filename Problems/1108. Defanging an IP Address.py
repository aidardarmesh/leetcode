class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")

s = Solution()
print(s.defangIPaddr("1.1.1.1"))

print(s.defangIPaddr("255.100.50.0"))