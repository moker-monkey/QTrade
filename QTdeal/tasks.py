from celery.app import shared_task

from .dealModel import Deal


class myDeal(Deal):
    def __init__(self):
        super().__init__()


# @shared_task(bind=True)
def test_deal():
    deal = Deal('test')
    # s = deal.buy('000001.SZ', '20190202', 24.14, 200, '我的第一次购买')
    deal.sell('000001.SZ', 3,'20190303', 28.12, 200)
