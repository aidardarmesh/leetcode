class Solution:
    def defangIPaddr(self, address: str) -> str:
        new_address = ""

        for ch in address:
            if ch == ".":
                new_address += "[.]"
            else:
                new_address += ch
        
        return new_address

s = Solution()
print(s.defangIPaddr("1.1.1.1"))

print(s.defangIPaddr("255.100.50.0"))