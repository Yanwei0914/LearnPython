"""
Give nums = [2,7,11,15], target = 9
num[0] + num[1] = 2 + 7 =9,
return [0,1]
"""
class Soulution:
    def twoSum(self, nums, target):
        for i in nums:
            j = target - i
            start_index = nums.index(i)
            next_index = start_index + 1
            temp_nums = nums[next_index: ]
            if j in temp_nums:
                return(nums.index(i), next_index + temp_nums.index(j))
            

class Soulution2:
    def twoSum(self, nums, target):
        dict = {}  # 初始化一个空字典，用于存储数组中数值及其索引
        for i in range(len(nums)):  # 遍历数组的索引 i
            if target - nums[i] not in dict:  # 如果目标值减去当前值的结果不在字典中
                dict[nums[i]] = i  # 将当前值及其索引存入字典
            else:  # 如果在字典中找到符合条件的数
                return [dict[target - nums[i]], i]  # 返回匹配数的索引和当前数的索引


"""
利用字典{"2":0, "7":1, "11":2, "15":3}
字典的键整数的时候，可以不加引号
{2:0, 7:1, 11:2, 15:3}
"""
