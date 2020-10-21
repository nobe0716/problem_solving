from bisect import bisect_right
from collections import defaultdict
from typing import List


class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        winner_vote_count = 0
        winner = None
        person_to_votes = defaultdict(int)
        self.winners = []
        self.timeline = []
        for person, time in zip(persons, times):
            person_to_votes[person] += 1
            if person_to_votes[person] >= winner_vote_count:
                winner_vote_count = person_to_votes[person]
                winner = person
            self.winners.append(winner)
            self.timeline.append(time)

    def q(self, t: int) -> int:
        idx = bisect_right(self.timeline, t)
        return self.winners[idx - 1]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)

ops = ["TopVotedCandidate", "q", "q", "q", "q", "q", "q"]
params = [[[0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30]], [3], [12], [25], [15], [24], [8]]

obj = TopVotedCandidate(*params[0])
for op, param in zip(ops[1:], params[1:]):
    print(obj.q(*param))
