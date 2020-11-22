from collections import defaultdict
from typing import List


class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        contents_to_paths = defaultdict(list)
        for path in paths:
            tokens = path.split(' ')
            directory = tokens[0]
            for e in tokens[1:]:
                file_name = e[:e.index('(')]
                file_content = e[e.index('('):-1]
                contents_to_paths[file_content].append(directory + '/' + file_name)

        res = []
        for k, v in contents_to_paths.items():
            if len(v) >= 2:
                res.append(v)
        return res
