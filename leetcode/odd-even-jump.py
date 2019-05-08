"""
## Name of Prob
975. Odd Even Jump

## Link
https://leetcode.com/problems/odd-even-jump/

## Note
At position i
odd jumps goes smallest j which A[i] <= A[j]
even jumps goes smallest j which A[i] >= A[j]

## Input
A ; Array of numbers

1 <= len(A) <= 20000
0 <= A[i] < 100000

## Output
N ; number of position which will be able to reach last position.

## Strategy

We need two array t_odd[i], t_even[i].
t_odd[i]; the number of path using odd jump to position i
t_even[i]; the number of path using even jump to position i

Make sorted set which contains unique number of given array.
Make dict value to indices of key in original array

For every A[i]
remove A[i] from indices in dict, and remove from sorted set when no index remains.
Be aware of using list.remove function because it takes O(N).
Use bisect.bisect_left instead.

Check whether there exist A[j] which has same value with A[i]
Then we should jump from i to j

Else, We find A[j] which is smallest and larger than A[i].
If it exists, t_even[i] should be added to t_odd[j]

Since we check the equality condition above,
we could be able to know that A[j - 1] must be less than A[i] but largest.
So A[i] will even jump if (j - 1) is valid index

### Complexity
First of all, it takes O(N log N) to sort key arrays
It takes O(1) to remove process, and it takes O(logN) to choose j from (odd|even)_key_arrays.
Above invariants will be done for i in range(N).
So total time complexity is expected to be O(N log N).

And Space complexity supposed to be O(N) cus k * N spaces will be needed for *_key_arrays, and dict
"""

_DEBUG = False

import bisect
from collections import Counter
from collections import defaultdict
from collections import deque
from typing import List

_DEBUG = False


class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        n = len(A)
        values = sorted(set(A))
        counter = Counter(A)

        pos_dict = defaultdict(deque)
        for i in range(n):
            pos_dict[A[i]].append(i)

        t_odd, t_even = [0] * n, [1] * n

        length_of_values = len(values)
        for i in range(n - 1):
            value = A[i]
            counter[value] -= 1
            if counter[value] == 0:
                # del pos_dict[value]
                values.pop(bisect.bisect_left(values, value))
                length_of_values -= 1
            else:
                pos_dict[value].popleft()

            smallest_pos = bisect.bisect_left(values, value)

            if smallest_pos < length_of_values and values[smallest_pos] == value:  # there exist same value
                first_pos_of_same_value = pos_dict[value][0]
                t_odd[first_pos_of_same_value] += t_even[i]
                t_even[first_pos_of_same_value] += t_odd[i]
                if _DEBUG:
                    print('odd-jump {}({}) to {}({})'.format(i, A[i], pos_dict[value][0], value))
                    print('even-jump {}({}) to {}({})'.format(i, A[i], pos_dict[value][0], value))
            else:
                if smallest_pos < length_of_values:
                    smallest_val = values[smallest_pos]
                    t_odd[pos_dict[smallest_val][0]] += t_even[i]
                    if _DEBUG:
                        print('odd-jump {}({}) to {}({})'.format(i, A[i], pos_dict[smallest_val][0], smallest_val))
                largest_pos = smallest_pos - 1
                if largest_pos >= 0 and t_odd[i] > 0:
                    largest_val = values[largest_pos]
                    t_even[pos_dict[largest_val][0]] += t_odd[i]
                    if _DEBUG:
                        print('even-jump {}({}) to {}({})'.format(i, A[i], pos_dict[largest_val][0], largest_val))
        return t_even[n - 1] + t_odd[n - 1]


s = Solution()
# assert s.oddEvenJumps([10, 13, 12, 14, 15]) == 2
# assert s.oddEvenJumps([2, 3, 1, 1, 4]) == 3
# assert s.oddEvenJumps([5, 1, 3, 4, 2]) == 3
