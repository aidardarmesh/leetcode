from typing import *

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniques = []

        for email in emails:
            local = ""
            at_index = email.find("@")
            domain = email[at_index+1:]

            for i in range(at_index):
                if email[i] == ".":
                    continue
                elif email[i] == "+":
                    break
                else:
                    local += email[i]
            
            new_email = local+"@"+domain
            
            if new_email not in uniques:
                uniques.append(new_email)
        
        return len(uniques)

s = Solution()

assert s.numUniqueEmails([
    "test.email+alex@leetcode.com",
    "test.e.mail+bob.cathy@leetcode.com",
    "testemail+david@lee.tcode.com"
]) == 2