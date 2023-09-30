"""
给你两个按 非递减顺序 排列的整数数组 nums1 和 nums2，另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。

请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。

注意：最终，合并后数组不应由函数返回，而是存储在数组 nums1 中。为了应对这种情况，nums1 的初始长度为 m + n，其中前 m 个元素表示应合并的元素，
后 n 个元素为 0 ，应忽略。nums2 的长度为 n 。


示例 1：

输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
输出：[1,2,2,3,5,6]
解释：需要合并 [1,2,3] 和 [2,5,6] 。
合并结果是 [1,2,2,3,5,6] ，其中斜体加粗标注的为 nums1 中的元素。


示例 2：

输入：nums1 = [1], m = 1, nums2 = [], n = 0
输出：[1]
解释：需要合并 [1] 和 [] 。
合并结果是 [1] 。


示例 3：

输入：nums1 = [0], m = 0, nums2 = [1], n = 1
输出：[1]
解释：需要合并的数组是 [] 和 [1] 。
合并结果是 [1] 。
注意，因为 m = 0 ，所以 nums1 中没有元素。nums1 中仅存的 0 仅仅是为了确保合并结果可以顺利存放到 nums1 中。
"""


def sort(list_data):
    for pointer in range(len(list_data)):
        if pointer == len(list_data) - 1:
            break
        if list_data[pointer] > list_data[pointer + 1]:
            swap(list_data, pointer, pointer + 1)
            # temp = list_data[pointer]
            # list_data[pointer] = list_data[pointer + 1]
            # list_data[pointer + 1] = temp
            sort(list_data)
            break


def partition(arr, left, right):
    index = left + 1
    i = index
    while i <= right:
        if arr[i] < arr[left]:
            swap(arr, i, index)
            index += 1
        i += 1
    swap(arr, left, index - 1)
    return index - 1


def quick_sort(arr, left=None, right=None):
    if not isinstance(left, (int, float)):
        left = 0
    if not isinstance(right, (int, float)):
        right = len(arr) - 1
    if left < right:
        partition_index = partition(arr, left, right)
        quick_sort(arr, left, partition_index - 1)
        quick_sort(arr, partition_index + 1, right)
    return arr


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

nums1[m:] = nums2
sort(nums1)
# quick_sort(nums1)
print(nums1)
