class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0
        right = len(nums) - 1

        while left != right:
            if nums[left] == 0:
                nums.append(nums.pop(left))
                right -= 1
            else:
                left += 1