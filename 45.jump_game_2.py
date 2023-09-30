"""
给定一个长度为 n 的 0 索引整数数组 nums。初始位置为 nums[0]。

每个元素 nums[i] 表示从索引 i 向前跳转的最大长度。换句话说，如果你在 nums[i] 处，你可以跳转到任意 nums[i + j] 处:

0 <= j <= nums[i]
i + j < n
返回到达 nums[n - 1] 的最小跳跃次数。生成的测试用例可以到达 nums[n - 1]。

示例 1:

输入: nums = [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。


示例 2:

输入: nums = [2,3,0,1,4]
输出: 2
"""


def jump_game(nums):
    size = len(nums)
    if size == 1:
        return 0
    times = 0
    jump_index = 0
    for i in range(size):
        if jump_index == i:
            times += 1
            element = 0
            for j in range(nums[i]):
                index = i + j + 1
                if index > size - 1:
                    index = size - 1
                if index + nums[index] >= element:
                    element = index + nums[index]
                    jump_index = index
            if i + nums[i] >= size - 1:
                return times


def jump_game_2(nums):  # 官方
    n = len(nums)
    maxPos, end, step = 0, 0, 0
    for i in range(n - 1):
        if maxPos >= i:
            maxPos = max(maxPos, i + nums[i])
            if i == end:
                end = maxPos
                step += 1
    return step


# nums = [2, 3, 1, 1, 4]
# nums = [2, 3, 0, 1, 4]
# nums = [1, 1, 2, 2, 0, 1, 1]
# nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 0]
nums = [7, 0, 9, 6, 9, 6, 1, 7, 9, 0, 1, 2, 9, 0, 3]
print(jump_game(nums))
