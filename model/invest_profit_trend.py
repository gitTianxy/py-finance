"""
给出各种可能的产品收益随时间变化趋势

将收益描述成时间的函数, 并提供指定时间间隔的采样序列
"""


class SinusoidalModel:
    """
    趋势随时间按正弦函数变化, 构建时指定振荡周期t
    """

    def __init__(self, t):
        if t < 1:
            raise TypeError('t should bigger than 1(a day)')
        self.t = t

    def daily_sampled(self):
        l = []
        return l

    def weekly_sampled(self):
        l = []
        return l

    def monthly_sampled(self):
        l = []
        return l
