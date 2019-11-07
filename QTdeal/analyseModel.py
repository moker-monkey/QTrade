import datetime
from datetime import timedelta

from dateutil.parser import parse
from dateutil.relativedelta import relativedelta


class StockBaseAnalyse(object):
    '''
    用以分析股票的基本面，价值投资所使用
    分析后落入数据库，以便查询分析
    '''

    def __init__(self, ts_code):
        self.ts_code = ts_code
        self.date = datetime.datetime.now().strftime('%Y%m%d')

    def get_quarter(self, state_dt):
        '''
        给任意时间点，能够获取到对应的财报时间,三种报告的当前已报告的时间，和未来
        强制报告时间是除中小板所有板块都必须发布的时间
        预告是有条件强制披露
        有条件披露：
        深圳主板：
        0. 针对所有报告期
        1. 归母净利润为负值
        2. 净利润同比上升/下降 50%
        3. 扭亏为赢
        4. 期末资产为负
        5. 年度营收低于一千万
        上海主板：
        1. 只针对年报预告
        2. 预计亏损
        3. 预计扭亏为盈
        4. 净利润同比变化50%

        中小板强制披露业绩快报，必须在2月底前披露，年度快报
        主板有可能披露快报，但是没有强制
        # 潜规则，年报需要预约，为了获取更多的资金，业绩越靠前的年报发布越早
        '''
        force_time = (('0430', '年报和一季度报'), ('0831', '中报'), ('1031', '三季报'))
        prophesy_time = (
            ('0131', '年报预告'),
            ('0415', '一季报预告'),
            ('0715', '中报预告'),
            ('1015', '三季报预告'),
        )
        tushare_period = (('0331', '一季报'), ('0630', '中报'), ('0930', '三季报'),
                          ('1231', '年报'))
        current_date = parse(state_dt)
        current_year = current_date.strftime('%Y')
        temp_date = None
        # 获取正报的时间
        for idx, val in enumerate(tushare_period):
            temp_date = parse(current_year + tushare_period[idx][0])
            next_date = parse(current_year + tushare_period[idx + 1][0])
            print(f'next_date:{next_date}')
            if current_date > temp_date and current_date < next_date:
                return {
                    'quarter': temp_date.strftime('%Y%m%d'),
                    'quarter_next': next_date.strftime('%Y%m%d')
                }
            else:
                return {
                    'quarter':
                    current_year + '1231',
                    'quarter_next': (parse(current_year + '0331') +
                                     relativedelta(years=1)).strftime('%Y%m%d')
                }

    def get_finance(self,ts_code,state_dt):
        '''
        获取快报，预报，正报的全部数据
        '''
        quarter = self.get_quarter(state_dt)
        finance = {
            'express':{},
            'forecast':{},
            'force':{}
        }

        

    def stock_sample(self):
        '''
        运行分析，并返回分析结果，结果是个包含检查项的dict，dict中的值为二进制，方便后面训练模型
        分析的维度有：
            1. 企业最近的财报的盈利同比
            2. 企业最近的财报的盈利环比
            3. 企业最近的预报，预增/预减
            4. 企业的 高转送 相关公告
            5. 企业的停牌等公告
            6. 企业的增减持
        '''
        return {''}

    def stock_info(self,ts_code,state_dt):
        '''
        获取具体信息，而非二进制：
        1. 企业最近的财报的盈利同比
        2. 企业最近的财报的盈利环比
        3. 企业最近的预报，预增/预减
        4. 企业的 高转送 相关公告
        5. 企业的停牌等公告
        6. 企业的增减持
        7. 企业的法院情况
        8. 企业高管的法院情况
        9. 企业相关新闻
        10.企业高层相关新闻
        11.企业行业相关新闻
        12.企业历史分红记录
        13.市盈率PE （最好5倍以内）
        14.净利润率
        15.负债
        16.政府相关度
        17.十大股东追踪（比如高领资本）
        18.每日龙虎榜（比如某抄家）
        '''

        return {}
