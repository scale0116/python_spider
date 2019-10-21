from __future__ import division

import tushare as ts
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = ts.get_hist_data('510050', '2017-01-01')
data = data.sort_index()
df = pd.DataFrame()
df['close'] = data['close']
df['change'] = df['close'] - df['close'].shift(1)
df = df.dropna()
# print(df)

# 定义数据缓存结构
close5_array = np.zeros(5)  # MA5缓存数组
close20_array = np.zeros(20)  # MA20缓存数组
last_signal = 0  # 最近的交易信号，初始化为0
last_pos = 0  # 最近的持仓，初始化为0

dr_list = []  # 每日盈亏结果列表


class DailyResult:
    """每日盈亏结果"""

    def __init__(self):
        """构造函数，初始化成员变量"""
        self.date = ''  # 日期
        self.close = 0  # 当日收盘
        self.change = 0  # 当日涨跌
        self.pos = 0  # 当日持仓
        self.last_pos = 0  # 昨日持仓

        self.pnl = 0  # 当日盈亏
        self.fee = 0  # 手续费
        self.net_pnl = 0  # 净盈亏

    def calculate(self, date, close, change, last_signal, last_pos):
        """计算每日盈亏"""
        # 赋值原始数据
        self.date = date
        self.close = close
        self.change = change
        self.pos = last_signal
        self.last_pos = last_pos

        # 计算结果数据
        self.pnl = self.change * self.pos
        self.fee = abs(self.pos - self.last_pos) * 1.5 / 10000  # ETF手续费万1.5
        self.net_pnl = self.pnl - self.fee


# 运行回测
for i, row in enumerate(df.iterrows()):
    date = row[0]
    close = row[1]['close']
    change = row[1]['change']

    # 将数组中的老数据平移一格
    close5_array[0:4] = close5_array[1:5]
    close20_array[0:19] = close20_array[1:20]

    # 将新数据添加到数组末尾
    close5_array[-1] = close
    close20_array[-1] = close

    # 如果尚未有20个数据点的缓存数量，则不执行后续逻辑
    if i < 20:
        continue

    # 计算当日持仓盈亏
    dr = DailyResult()
    dr.calculate(date, close, change, last_signal, last_pos)

    # 保存计算结果到列表中
    dr_list.append(dr)

    # 记录当日的持仓
    last_pos = dr.pos

    # 计算信号数据
    ma5 = close5_array.mean()
    ma20 = close20_array.mean()
    if ma5 >= ma20:
        last_signal = 10000
    else:
        last_signal = -10000


# 显示回测结果
result_df = pd.DataFrame()
result_df['net_pnl'] = [dr.net_pnl for dr in dr_list]   # 将DailyResult列表中的数据转换为DataFrame格式
result_df.index = [dr.date for dr in dr_list]           # 添加日期索引

result_df['cum_pnl'] = result_df['net_pnl'].cumsum()     # 累积求和
result_df['cum_pnl'].plot()
plt.show()