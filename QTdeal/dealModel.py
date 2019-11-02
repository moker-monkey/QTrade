import datetime

from dateutil.relativedelta import relativedelta
from dateutil.parser import parse
from django.db.models import Q
import pandas as pd

from .models import MyCapital, MyStockPool
from sync_db.models import SyncDataDailyBasic


class Deal():
    '''
    买就是对总表和买入表进行写入操作，
    主要用于每一次回测都是使用一个新的deal实例，可灵活掌握初始资金，方便计算
    同一只股票有可能多次买卖，并不一定所有的买单都会被平仓，因此需要在策略中进行控制
    '''

    def __init__(self, name, capital=100000):
        self.name = name
        self.capital = capital
        self.money_lock = 0

    def create_capital(self, ts_code, deal_action, deal_price, stock_vol, bz,
                       state_dt, serial):
        self.money_lock = deal_price * stock_vol
        self.capital = eval(
            f"{self.capital} {'-' if deal_action == 'buy' else '+'} {self.money_lock}"
        )
        hold_days = 0
        profit = 0
        profit_rate = 0
        # TODO 给Stockpool加上开仓时间，方便计算
        # deal_price是整数，改成实数
        # 错误，stockpool 没有state_dt字段
        if deal_action == 'sell':
            buy = MyStockPool.objects.get(id=serial)
            profit = buy.buy_price * buy.hold_vol - self.money_lock
            profit_rate = profit / self.capital
            hold_days = (parse(state_dt) - parse(buy.state_dt)).days
        params = {
            'name': self.name,
            'capital': self.capital,
            'money_lock': self.money_lock,
            'money_rest': self.capital - self.money_lock,
            'deal_action': deal_action,
            'ts_code': ts_code,
            'deal_price': deal_price,
            'stock_vol': stock_vol,
            'profit': profit,
            'profit_rate': profit_rate,
            'state_dt': state_dt,
            'bz': bz,
            'hold_days': hold_days,
            'serial': serial
        }
        mc = MyCapital(**params)
        mc.save()
        return mc

    def add_stock_pool(self, ts_code, buy_price, hold_vol, hold_days=1):
        msp = MyStockPool(
            **{
                'ts_code': ts_code,
                'buy_price': buy_price,
                'hold_vol': hold_vol,
                'hold_days': hold_days
            })
        msp.save()
        return msp

    def remove_stock_pool(self, serial):
        msp = MyStockPool.objects.get(id=serial).delete()
        print(f'serial with {serial} remove is success')

    def clearCapital(self, name=''):
        if name:
            MyCapital.objects.get(name=name).delete()
            print(f'MyCapital with {name} is delete')
        else:
            MyCapital.objects.all().delete()
            print('MyCapital is clear')

    def buy(
            self,
            ts_code,
            opdate,
            price,
            vol,
            bz='',
    ):
        # 创建一条capital和MyStockPool，返回id
        serial = self.add_stock_pool(ts_code, price, vol).id
        self.create_capital(ts_code, 'buy', price, vol, bz, opdate, serial)
        return serial

    def sell(
            self,
            ts_code,
            serial,
            opdate,
            price,
            vol,
            bz='',
    ):
        # 获取pool_id,删除myStockpool中对应的记录
        # 添加一条myCapital记录
        #TODO 这里可能会导致已经记录了，但是未能删除
        self.create_capital(
            ts_code=ts_code,
            deal_action='sell',
            deal_price=price,
            stock_vol=vol,
            bz=bz,
            state_dt=opdate,
            serial=serial)
        self.remove_stock_pool(serial)
        return serial

    def get_stock(self, trade_date):
        '''用于选取股票,返回ts_code,可在使用时重新定义'''
        return ''

    def tactics(self, buy, sell, ts_code, trade_date):
        '''
        buy&sell是回调函数，可以方便的重写策略
        策略包括：选股初始化模块/交易预警模块/买卖点判断模块/仓位管理/交易执行模块
        '''
        return ''

    def test_deal(self, start_date, end_date, freq='D', periods=10):
        '''
        该测试函数是为了模拟真实的交易环境，其配合交易日历，新闻，公司报告等函数进行
        '''
        datetime_index = pd.date_range(start_date, end_date, periods, freq)
        for i, v in enumerate(datetime_index):
            # v.date()是datetime对象
            ts_code = self.get_stock(v.date())
            # 交易策略模块
            self.tactics(self.buy, self.sell, ts_code, v.date())
            # 模型训练模块
