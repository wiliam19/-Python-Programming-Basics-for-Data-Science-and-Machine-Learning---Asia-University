class Solution:
	def twoSum(self, nums, target):
		li = []
		for index in range(len(nums)):
			tmp_tuple = (index,nums[index])
			li.append(tmp_tuple)
		li = sorted(li,key=lambda x:x[1])
		n = 0
		m = len(nums)-1

		while True:
			if li[n][1] + li[m][1] == target:
				return [li[n][0],li[m][0]]
			elif li[n][1] + li[m][1] < target:
				n = n + 1
			else:
				m = m - 1

so = Solution()
print(so.twoSum([2,1,9,4,4,56,90,3],8))