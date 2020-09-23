import re

fd = open('regex_sum_810750.txt', 'r')
nums = list()
for line in fd:
	new_num = re.findall('[0-9]+', line)
	nums += new_num
i = 0
len_nums = len(nums)
while i < len_nums:
	nums[i] = int(nums[i])
	i += 1
print(sum(nums))
