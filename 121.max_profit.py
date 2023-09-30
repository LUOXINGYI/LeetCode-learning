"""
给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。

你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。

返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。

示例 1：

输入：[7,1,5,3,6,4]
输出：5
解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。


示例 2：

输入：prices = [7,6,4,3,1]
输出：0
解释：在这种情况下, 没有交易完成, 所以最大利润为 0。
"""


def max_profit(prices):
    price_map = {}
    index = 0
    for i in prices:
        if 'max' not in price_map.keys():
            price_map['max'] = i
            price_map['max-index'] = index
        if 'min' not in price_map.keys():
            price_map['min'] = i
            price_map['min-index'] = index
            price_map['profit'] = 0
        if i < price_map['min'] and index != len(prices) - 1:
            price_map['min'] = i
            price_map['min-index'] = index
            price_map['max'] = i
            price_map['max-index'] = index
        if i > price_map['max']:
            price_map['max'] = i
            price_map['max-index'] = index
            profit = price_map['max'] - price_map['min']
            if profit > price_map['profit']:
                price_map['profit'] = profit
        index += 1
    if price_map['max-index'] > price_map['min-index']:
        if price_map['profit'] != 0:
            return price_map['profit']
        return 0
    else:
        profit = price_map['max'] - price_map['min']
        if profit > price_map['profit']:
            return profit
        else:
            return price_map['profit']


# prices = [7, 1, 5, 3, 6, 4]
# prices = [2, 4, 1]
# prices = [3, 2, 6, 5, 0, 3]
prices = [4, 7, 2, 1]
print(max_profit(prices))
