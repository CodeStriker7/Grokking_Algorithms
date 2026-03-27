class Solution:
	def searchbinary(self, nums: list[int], target: int) -> int:
		low = 0
		high = len(nums) - 1
		while low <= high:
			med = (low + high) // 2
			guess = nums[med]
			if target == guess:
				return med
			if target < guess:
				high = med - 1
			else:
				low = med + 1
		return low  

nums = [1,2,3,4,5,6]
guess = int(input("need number enter: "))
target = guess

obj = Solution()
solve = obj.searchbinary(nums, target)
print (solve)