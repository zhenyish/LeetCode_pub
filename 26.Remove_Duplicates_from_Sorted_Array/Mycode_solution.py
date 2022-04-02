class Solution(object):
    "Time: O(N)"
    "Space: O(1)"
    def removeDuplicates(self, nums):
        "unique is to track the current unique element"
        "Here initialize unique as None since we don't know which type of element in the List"
        unique = None
        "k is to track the number of unique values"
        k = 0
        for i in range(len(nums)):
            if (unique != nums[i]):
                unique = nums[i]
                k += 1
                nums[k-1] = unique
        return k
        """
        :type nums: List[int]
        :rtype: int
        """
