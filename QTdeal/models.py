from django.db import models


# Create your models here.
class MyCapital(models.Model):
    '''
    账本表（记录每一次的买和卖的操作）
    '''
    name = models.CharField(verbose_name='名称', max_length=100, blank=True)
    capital = models.FloatField(verbose_name='总资产')
    money_lock = models.FloatField(verbose_name='股票资产')
    money_rest = models.FloatField(verbose_name='现金资产')
    deal_action = models.CharField(verbose_name='交易动作', max_length=100)
    ts_code = models.CharField(verbose_name='股票代码', max_length=100)
    deal_price = models.FloatField(verbose_name='成交价')
    stock_vol = models.IntegerField(verbose_name='成交量(股)')
    profit = models.FloatField(verbose_name='收益额', null=True, blank=True)
    profit_rate = models.FloatField(
        verbose_name='收益率', null=True, blank=True)
    bz = models.CharField(
        verbose_name='备注', max_length=300, null=True, blank=True)
    state_dt = models.CharField(verbose_name='交易日期', max_length=100)
    hold_days = models.IntegerField(verbose_name='持有时间', null=True, blank=True,default=0)
    serial = models.IntegerField(
        verbose_name='序列号')  # 买和卖共用一组序列号,存的是MyStockPool的id


class MyStockPool(models.Model):
    ts_code = models.CharField(verbose_name='股票代码', max_length=100)
    buy_price = models.FloatField(verbose_name='买入价格')
    hold_vol = models.IntegerField(verbose_name='持仓量（股）')
    hold_days = models.IntegerField(verbose_name='持仓天数')
    opdate = models.CharField(verbose_name='开仓时间',max_length=100,default='')
