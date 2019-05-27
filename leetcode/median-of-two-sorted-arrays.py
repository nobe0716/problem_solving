"""
## Name of Prob
Median of Two Sorted Arrays

## Link
https://leetcode.com/problems/median-of-two-sorted-arrays/

## Note
Median; values which divides array two equal-sized sub-arrays
    - odd size, median belong to given array
    - even size, median is half of mid two values

'Two' sorted arrays (individually sorted)

- there are (len(A) + len(B)) // 2 number, which are smaller than median

## Input
num1, num2

## Output
median of two sorted array

## Strategy
let half = (len(A) + len(B) + 1) // 2,

Suppose len(A) < len(B) for convenience, we can swap if len(A) > len(B)

First find valid index 'i' of A and 'j' of B
A[:i], B[:j] values will be smaller than median
num1[i] >= num2[j - 1], num1[i - 1] <= num2[j]

Use binary search to find i on A
j is determined by i, i + j == (m + n + 1) // 2 => j = (m + n + 1) // 2 - i


then infer median or two mid values from i and j

"""


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        m, n = len(nums1), len(nums2)
        if m > n:
            m, n, nums1, nums2 = n, m, nums2, nums1
        lo, hi = 0, m
        half = (m + n + 1) // 2
        while lo <= hi:
            i = (lo + hi) // 2
            j = half - i

            if i < hi and nums1[i] < nums2[j - 1]:
                lo = i + 1
            elif i > lo and nums1[i - 1] > nums2[j]:
                hi = i - 1
            else:
                left_highest = None
                if i == 0:
                    left_highest = nums2[j - 1]
                elif j == 0:
                    left_highest = nums1[i - 1]
                else:
                    left_highest = max(nums1[i - 1], nums2[j - 1])

                if (m + n) % 2 == 1:
                    return left_highest * 1.0

                right_smallest = None
                if i == m:
                    right_smallest = nums2[j]
                elif j == n:
                    right_smallest = nums1[i]
                else:
                    right_smallest = min(nums1[i], nums2[j])
                # print(left_highest, right_smallest)
                return (left_highest + right_smallest) / 2.0


solution = Solution()
assert solution.findMedianSortedArrays([1, 3], [2]) == 2.0
assert solution.findMedianSortedArrays([1, 4], [2, 3]) == 2.5
