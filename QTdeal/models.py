from django.db import models


# Create your models here.
class MyCapital(models.Model):
    '''
    账本表（记录每一次的买和卖的操作）
    '''
    capital = models.IntegerField(verbose_name='总资产')
    money_lock = models.IntegerField(verbose_name='股票资产')
    money_rest = models.IntegerField(verbose_name='现金资产')
    deal_action = models.CharField(verbose_name='交易动作', max_length=100)
    ts_code = models.CharField(verbose_name='股票代码', max_length=100)
    deal_price = models.IntegerField(verbose_name='成交价')
    stock_vol = models.IntegerField(verbose_name='成交量(手)')
    profit = models.IntegerField(verbose_name='收益额',null=True,blank=True)
    profit_rate = models.IntegerField(verbose_name='收益率',null=True,blank=True)
    bz = models.CharField(verbose_name='备注', max_length=300,null=True,blank=True)
    state_dt = models.CharField(verbose_name='交易日期', max_length=100)
    hold_days = models.IntegerField(verbose_name='持有时间',null=True,blank=True)
    serial = models.IntegerField(verbose_name='序列号') # 买和卖共用一组序列号,存的是MyStockPool的id

class MyStockPool(models.Model):
    ts_code = models.CharField(verbose_name='股票代码',max_length=100)
    buy_price = models.IntegerField(verbose_name='买入价格')
    hold_vol = models.IntegerField(verbose_name='持仓量')
    hold_days = models.IntegerField(verbose_name='持仓天数')
