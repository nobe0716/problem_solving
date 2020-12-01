"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""
from typing import List


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        def traverse(node: int) -> int:
            return d[node].importance + sum(traverse(_) for _ in d[node].subordinates)

        d = {employee.id: employee for employee in employees}
        return traverse(id)
