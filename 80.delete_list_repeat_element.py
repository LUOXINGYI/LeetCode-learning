"""
给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使得出现次数超过两次的元素只出现两次 ，返回删除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

示例 1：

输入：nums = [1,1,1,2,2,3]
输出：5, nums = [1,1,2,2,3]
解释：函数应返回新长度 length = 5, 并且原数组的前五个元素被修改为 1, 1, 2, 2, 3。 不需要考虑数组中超出新长度后面的元素。
示例 2：

输入：nums = [0,0,1,1,1,1,2,3,3]
输出：7, nums = [0,0,1,1,2,3,3]
解释：函数应返回新长度 length = 7, 并且原数组的前五个元素被修改为 0, 0, 1, 1, 2, 3, 3。不需要考虑数组中超出新长度后面的元素。
"""

nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]

fastPointer = 1
slowPointer = 1
switch = 1

while fastPointer < len(nums):
    if nums[fastPointer] == nums[fastPointer - 1]:
        if switch >= 2:
            pass
        else:
            nums[slowPointer] = nums[fastPointer]
            slowPointer += 1
            switch += 1
    else:
        nums[slowPointer] = nums[fastPointer]
        slowPointer += 1
        switch = 1
    fastPointer += 1

print(nums[:slowPointer])