from typing import *

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs, digit_logs = [], []
        ids = {}
        
        for log in logs:
            first_space = log.find(' ')
            
            if log[first_space+1].isdigit():
                digit_logs.append(log)
            else:
                ids[log] = first_space+1
                letter_logs.append(log)
        
        return sorted(letter_logs, key=lambda x: (x[ids[x]:], x[:ids[x]])) + digit_logs
