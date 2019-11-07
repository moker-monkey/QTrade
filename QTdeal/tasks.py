from celery.app import shared_task

from .dealModel import Deal


class MyDeal(Deal):
    def __init__(self, name, capital=100000):
        super().__init__(name=name, capital=capital)


    def tactics(self, buy, sell, ts_code, trade_date):
        s = buy('000001.SZ', '20190202', 24.14, 200, '我的第一次购买')
        sell('000001.SZ', s, '20190303', 28.12, 200)


# @shared_task(bind=True)
def test_deal():
    deal = MyDeal('test-one')
    deal.test_deal(start_date='20190201', end_date='20190330')
