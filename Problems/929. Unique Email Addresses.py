from typing import *

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniques = []

        for email in emails:
            at_index = email.find("@")
            domain = email[at_index+1:]
            local = email[:at_index]
            plus_index = local.find("+")
            
            if plus_index > -1:
                local = local[:plus_index]

            local = local.replace(".", "")
            
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