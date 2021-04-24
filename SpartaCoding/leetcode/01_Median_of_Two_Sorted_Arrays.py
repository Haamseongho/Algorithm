from typing import List

input1 = [1, 2]
input2 = [3, 4]


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        median = 0
        m = len(nums1)
        if (m / 2) == 0:
            n = (0 + len(nums1) - 1) // 2
            median = (nums1[n] + nums1[n + 1]) / 2

        else:
            n = int((0 + len(nums1) - 1) / 2)
            median = nums1[n]

        return median


s = Solution()
ans = s.findMedianSortedArrays(input1, input2)
print(ans)
