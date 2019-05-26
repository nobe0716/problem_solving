class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        num1, num2 = nums1, nums2
        if len(num1) > len(num2):
            num1, num2 = num2, num1
        m, n = len(num1), len(num2)
        half_len = (n + m + 1) // 2

        lo, hi = 0, m

        while lo <= hi:
            mid = (lo + hi) // 2
            j = half_len - mid

            if mid < hi and num2[j - 1] > num1[mid]:
                lo = mid + 1
            elif mid > lo and num2[j] < num1[mid - 1]:
                hi = mid - 1
            else:
                max_left = 0
                if mid == 0:
                    max_left = num2[j - 1]
                elif j == 0:
                    max_left = num1[mid - 1]
                else:
                    max_left = max(num1[mid - 1], num2[j - 1])

                if (m + n) % 2 == 1:
                    return max_left * 1.0

                min_right = 0
                if mid == m:
                    min_right = num2[j]
                elif j == n:
                    min_right = num1[mid]
                else:
                    min_right = min(num1[mid], num2[j])
                # print(max_left, min_right)
                return (max_left + min_right) / 2.0
        return 0


solution = Solution()
print(solution.findMedianSortedArrays([1, 4], [2, 3]))
