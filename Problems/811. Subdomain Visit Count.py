from typing import *

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        res, counter = [], {}

        for count_domain in cpdomains:
            count, domain = count_domain.split()

            while True:
                count = int(count)
                
                if domain in counter:
                    counter[domain] += count
                else:
                    counter[domain] = count
                
                dot_pos = domain.find('.')

                if dot_pos == -1:
                    break
                
                domain = domain[dot_pos+1:]
        
        for domain in counter:
            res.append(str(counter[domain]) + ' ' + domain)
        
        return res

s = Solution()

assert s.subdomainVisits(["9001 discuss.leetcode.com"]) == ["9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"]
assert s.subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]) == \
    ["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]