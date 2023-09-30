"""
给你一个非负整数数组 nums ，你最初位于数组的 第一个下标 。数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个下标，如果可以，返回 true ；否则，返回 false 。

示例 1：

输入：nums = [2,3,1,1,4]
输出：true
解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。


示例 2：

输入：nums = [3,2,1,0,4]
输出：false
解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。
"""


def jump_game(nums):
    size = len(nums)
    if size == 1:
        return True
    if nums[0] == 0:
        return False
    for i in range(size):
        if nums[i] >= size - i:
            return True
        if nums[i] == 0 and i != size - 1:
            num = 1
            switch = True
            for j in range(i + 1):
                if j == 0:
                    continue
                if nums[i - j] > num:
                    switch = False
                    break
                num += 1
            if switch:
                return False
    return True


def can_jump(nums):  # 贪心算法
    n, rightmost = len(nums), 0
    for i in range(n):
        if i <= rightmost:
            rightmost = max(rightmost, i + nums[i])
            if rightmost >= n - 1:
                return True
    return False


# nums = [2, 3, 1, 1, 4]
# nums = [3, 2, 1, 0, 4]
# nums = [0, 1]
# nums = [0]
# nums = [1, 1, 2, 2, 0, 1, 1]
nums = [1, 1, 0, 1]
print(jump_game(nums))
