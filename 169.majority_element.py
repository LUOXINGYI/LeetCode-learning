"""
给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

示例 1：

输入：nums = [3,2,3]
输出：3


示例 2：

输入：nums = [2,2,1,1,1,2,2]
输出：2
"""


def majority_element(nums):
    if len(nums) == 1:
        return nums[0]
    num_map = {}
    end_size = len(nums) / 2
    for i in nums:
        if i in num_map.keys():
            num_map[i] += 1
            if num_map[i] > end_size:
                return i
        else:
            num_map[i] = 1


nums = [1]
print(majority_element(nums))
