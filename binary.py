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

# Recap
# • Binary search is a lot faster than simple search.
# • O(log n) is faster than O(n), but it gets a lot faster once the list of
# items you’re searching through grows.
# • Algorithm speed isn’t measured in seconds.
# • Algorithm times are measured in terms of growth of an algorithm.
# • Algorithm times are written in Big O notation.