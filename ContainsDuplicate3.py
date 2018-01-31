class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if len(nums) > 1:
            for x in range(0, len(nums) - 1):
                for y in range(x + 1, min(x + k + 1, len(nums))):
                    if abs(nums[y] - nums[x]) <= t:
                        return True
        return False


test = Solution()
print(test.containsNearbyAlmostDuplicate([-1, -1], 1, 0))
