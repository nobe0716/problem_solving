from collections import defaultdict
from operator import itemgetter
from typing import List


class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        num_of_candidates = len(votes[0])
        score_dict = defaultdict(lambda: [0] * num_of_candidates + [0])
        for vote in votes:
            for i, v in enumerate(vote):
                score_dict[v][i] += 1
        for k in score_dict.keys():
            score_dict[k][num_of_candidates] = -ord(k)
        # print(score_dict.items())
        sorted_items = sorted(score_dict.items(), key=itemgetter(1), reverse=True)
        # print(sorted_items)
        return ''.join(list(map(itemgetter(0), sorted_items)))


if __name__ == '__main__':
    s = Solution()
    # assert s.rankTeams(votes=["ABC", "ACB", "ABC", "ACB", "ACB"]) == "ACB"
    # assert s.rankTeams(votes=["WXYZ","XYZW"]) == "XWYZ"
    assert s.rankTeams(["BCA", "CAB", "CBA", "ABC", "ACB", "BAC"]) == "ABC"
