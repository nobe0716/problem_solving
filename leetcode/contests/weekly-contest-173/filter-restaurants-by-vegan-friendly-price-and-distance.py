from operator import itemgetter
from typing import List


class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> \
            List[int]:
        res = restaurants
        if veganFriendly == 1:
            res = list(filter(lambda x: x[2] == 1, res))
        res = list(filter(lambda x: x[3] <= maxPrice and x[4] <= maxDistance, res))
        res = sorted(res, key=itemgetter(1, 0), reverse=True)
        return list(map(itemgetter(0), res))
