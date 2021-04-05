from collections import defaultdict
from typing import List, Set


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        name_to_email_groups = defaultdict(list)
        for account_info in accounts:
            name = account_info[0]
            emails = set(account_info[1:])
            name_to_email_groups[name].append(emails)

        def union_sets(email_sets: List[Set[str]]) -> List[List[str]]:
            n = len(email_sets)
            g = defaultdict(set)

            for i in range(n - 1):
                for j in range(i + 1, n):
                    if email_sets[i].intersection(email_sets[j]):
                        g[i].add(j)
                        g[j].add(i)

            groups = []
            visited = set()
            for i in range(n):
                if i in visited:
                    continue
                group = {i}
                stack = [i]
                while stack:
                    j = stack.pop()
                    for k in g[j]:
                        if k not in group:
                            group.add(k)
                            stack.append(k)

                email_set = set()
                visited = visited.union(group)
                for j in group:
                    email_set = email_set.union(email_sets[j])
                groups.append(sorted(email_set))
            return groups

        res = []
        for name, email_sets in name_to_email_groups.items():
            email_groups = union_sets(email_sets)
            for email_group in email_groups:
                res.append([name] + email_group)
                # print(name, email_group)

        return res


s = Solution()
assert s.accountsMerge(accounts=[["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["John", "johnsmith@mail.com", "john00@mail.com"], ["Mary", "mary@mail.com"], ["John", "johnnybravo@mail.com"]]) == \
       [["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"],
        ["Mary", "mary@mail.com"],
        ["John", "johnnybravo@mail.com"]]
