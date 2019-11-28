from typing import *

"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        id_imp, id_subs, total_imp = {}, {}, 0
        
        for emp in employees:
            id_imp[emp.id] = emp.importance
            id_subs[emp.id] = emp.subordinates
        
        queue = [id]
        
        while queue:
            size = len(queue)
            
            for _ in range(size):
                id_ = queue.pop(0)
                total_imp += id_imp[id_]
                queue += id_subs[id_]
        
        return total_imp
