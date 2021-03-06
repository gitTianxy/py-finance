"""
假设
我把300元钱均分成3份去买'月'为周期的理财产品;
一开始把它们平均地投在一个月的1,11,21三个日期;
之后如果有更好的产品, 我将投入100元, 并退出此后紧邻到期的产品.

容易想见
如果一味追求高收益, 一有好产品就去投, 那么随着时间的推移, 起息日将不再以10为间隔平均分布在一个月中.
所以, "高收益"和"均匀投资"这两个投资目标之间虽然没有关联, 却是有可能相互背离的; 所以实际采取的策略应该兼顾两者, 需要给出一个函数来做综合评定.
基于这样的认识, 至少可以采取如下几种策略:
1. 只求高收益,不顾时间分布
2. 优先保证时间分布, 如果在此条件下有高收益机会则及时出手
3. 容忍一定程度的时间分布不均匀, 同时这样也牺牲了部分的利益
针对上述策略, 有如下的分析

I. 收益优先策略分析
计算最终一年的收益, 以及时间上有多少次不均匀分布(多少天用钱危机)

II. 时间分布优先策略分析
每次购买的起息日期均分一个月, 例如按照如下序列增长:
[01,11,21]
[01,11,21,'26']
[01,'06',11,21,26]
[01,06,11,'16',21,26]
[01,06,11,16,'19',21,26]
[01,06,11,16,19,21,'23',26]
[01,'03',06,11,16,19,21,23,26]
[01,03,06,'09',11,16,19,21,23,26]
[01,03,06,09,11,'13',16,19,21,23,26]
[01,03,06,09,11,13,16,19,21,23,26,'29']
[02,12,22]
[02,12,22,'27']
[02,'07',12,22,27]
[02,07,12,'17',22,27]
[02,07,12,17,'20',22,27]
[02,07,12,17,20,22,'24',27]
[02,07,12,17,20,22,24,27,'30']
[02,'04',07,12,17,20,22,24,27,30]
[02,04,07,'10',12,17,20,22,24,27,30]
[02,04,07,10,12,'14',17,20,22,24,27,30]
[05,15,25]
[08,18,28]

III. 兼容策略分析
A. 设定一个阈值, 如果起息日之间的分布不均衡程度(起息日间距较平均间距的方差)大于该阈值, 则停止下一轮投资. 问:
1. 第一次达到阈值平均经理多少轮投资?
2. 按照上述投资规则, 一年当中共计多少次投资?(因为每次投都是因为能获利更多,所以此次数越多, 代表获利机会多)
3. 如果把份数设置成变量n, 那么怎样的划分能使如'2'所述的一年当中的投资次数最大?
B. 把钱分成'闲余池','固定金','活动金'三类:
1. 保证在每个月1,11,21日有固定金(除非遇到更有利且同时稳定的产品可被替换)
2. 闲余池用于购买高收益产品, 其金额需比固定金的每份稍大以保证能买得动新的固定金产品; 需要注意的是, 当用它买入新的产品而余额小于固定金后, 需要用之后对应的产品来补充--固定金产品用之后到期的固定金补, 活动金产品用到期活动金补.
3. 活动金和固定金相对, 表示一些临时性的优惠产品; 由于有了固定金的保证, 其起息日期可以是一个月中的任何一天

结论
1. 采取策略1的场景: ...
2. 采取策略2的场景: 无
3. 采取策略3的场景: ...
"""
product_dates = []


def product_dates():
    """
    平均分布地生成一年中产品的发布日期
    :return:
    """
    global product_dates

    pass


def count_moneyshort_day():
    """

    :return:
    """


if __name__ == '__main__':
    pass
