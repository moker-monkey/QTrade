import datetime

from dateutil.relativedelta import relativedelta
from dateutil.parser import parse

from .models import MyCapital, MyStockPool


class Deal():
    '''
    买就是对总表和买入表进行写入操作，
    主要用于每一次回测都是使用一个新的deal实例，可灵活掌握初始资金，方便计算
    同一只股票有可能多次买卖，并不一定所有的买单都会被平仓，因此需要在策略中进行控制
    '''

    def __init__(self, capital=100000):
        self.capital = capital
        self.money_lock = 0

    def create_capital(self, ts_code, deal_action, deal_price, stock_vol, bz,
                       state_dt, serial):
        self.money_lock = deal_price * stock_vol
        self.capital = eval(
            f"{self.capital} {'-' if deal_action == 'buy' else '+'} {self.money_lock}"
        )
        if deal_action == 'sell':
            buy = MyStockPool.objects.get(id=serial)
            profit = buy.buy_price * buy.hold_vol - self.money_lock
            profit_rate = profit / self.capital
            hold_days = (parse(state_dt) - parse(buy.state_dt)).days
        params = {
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
        msp = MyStockPool(**{
            'ts_code': ts_code,
            'buy_price': buy_price,
            'hold_vol': hold_vol
        })
        msp.save()
        return msp

    def remove_stock_pool(self, serial):
        msp = MyStockPool.objects.delete(id=serial)
        msp.save()

    def buy(
            self,
            ts_code,
            opdate,
            price,
            vol,
            bz,
    ):
        # 创建一条capital和MyStockPool，返回id
        serial = self.add_stock_pool(ts_code, price, vol).id
        self.create_capital(ts_code, 'buy', price, vol, bz, opdate, serial)

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
        self.remove_stock_pool(serial)
        self.create_capital(ts_code, 'sell', price, vol, bz, opdate, serial)
