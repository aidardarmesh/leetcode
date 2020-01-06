from typing import *

class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        data = collections.defaultdict(list)
        ans = set()
        
        for transaction in transactions:
            name, time, amount, city = transaction.split(',')
            time, amount = int(time), int(amount)
            
            if amount > 1000:
                ans.add(transaction)
            
            for prev in data[name]:
                if abs(time-prev['time']) <= 60 and city != prev['city']:
                    ans.add(transaction)
                    ans.add(
                        ','.join([
                            name,
                            str(prev['time']),
                            str(prev['amount']),
                            prev['city']
                        ])
                    )
            
            data[name].append({'time':time,'amount':amount,'city':city})
        
        return ans
