# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class SyncDataDailyBasic(models.Model):
    field_id = models.AutoField(
        db_column='_id',
        primary_key=True)  # Field renamed because it started with '_'.
    ts_code = models.CharField(max_length=100)
    trade_date = models.CharField(max_length=100)
    close = models.FloatField(blank=True, null=True)
    turnover_rate = models.FloatField(blank=True, null=True)
    turnover_rate_f = models.FloatField(blank=True, null=True)
    volume_ratio = models.FloatField(blank=True, null=True)
    pe = models.FloatField(blank=True, null=True)
    pe_ttm = models.FloatField(blank=True, null=True)
    pb = models.FloatField(blank=True, null=True)
    ps = models.FloatField(blank=True, null=True)
    ps_ttm = models.FloatField(blank=True, null=True)
    total_share = models.FloatField(blank=True, null=True)
    float_share = models.FloatField(blank=True, null=True)
    free_share = models.FloatField(blank=True, null=True)
    total_mv = models.FloatField(blank=True, null=True)
    circ_mv = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'sync_data_daily_basic'


class SyncDataNews(models.Model):
    datetime = models.CharField(max_length=100,blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    title = models.CharField(
        primary_key=True, default='000000', max_length=200)

    class Meta:
        db_table = 'sync_data_news'


class SyncDataShibor(models.Model):
    date = models.CharField(
        primary_key=True, default='00000000', max_length=100)
    on = models.FloatField(blank=True, null=True)
    number_1w = models.FloatField(
        db_column='1w', blank=True, null=True
    )  # Field renamed because it wasn't a valid Python identifier.
    number_2w = models.FloatField(
        db_column='2w', blank=True, null=True
    )  # Field renamed because it wasn't a valid Python identifier.
    number_1m = models.FloatField(
        db_column='1m', blank=True, null=True
    )  # Field renamed because it wasn't a valid Python identifier.
    number_3m = models.FloatField(
        db_column='3m', blank=True, null=True
    )  # Field renamed because it wasn't a valid Python identifier.
    number_6m = models.FloatField(
        db_column='6m', blank=True, null=True
    )  # Field renamed because it wasn't a valid Python identifier.
    number_9m = models.FloatField(
        db_column='9m', blank=True, null=True
    )  # Field renamed because it wasn't a valid Python identifier.
    number_1y = models.FloatField(
        db_column='1y', blank=True, null=True
    )  # Field renamed because it wasn't a valid Python identifier.

    class Meta:
        db_table = 'sync_data_shibor'


class SyncDataStock5Minute(models.Model):
    ts_code = models.TextField(blank=True, null=True)
    trade_time = models.CharField(
        primary_key=True, default='000000', max_length=100)
    open = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    vol = models.FloatField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    ma10 = models.FloatField(blank=True, null=True)
    ma_v_10 = models.FloatField(blank=True, null=True)
    ma20 = models.FloatField(blank=True, null=True)
    ma_v_20 = models.FloatField(blank=True, null=True)
    ma30 = models.FloatField(blank=True, null=True)
    ma_v_30 = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'sync_data_stock_5minute'


class SyncDataStockBasic(models.Model):
    ts_code = models.CharField(
        primary_key=True, default='000000', max_length=100)
    symbol = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    area = models.TextField(blank=True, null=True)
    industry = models.TextField(blank=True, null=True)
    list_date = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'sync_data_stock_basic'


class SyncDataStockDay(models.Model):
    trade_date = models.CharField(
        primary_key=True, default='000000', max_length=100)
    ts_code = models.TextField(blank=True, null=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    pre_close = models.FloatField(blank=True, null=True)
    change = models.FloatField(blank=True, null=True)
    pct_chg = models.FloatField(blank=True, null=True)
    vol = models.FloatField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    turnover_rate = models.FloatField(blank=True, null=True)
    volume_ratio = models.FloatField(blank=True, null=True)
    ma10 = models.FloatField(blank=True, null=True)
    ma_v_10 = models.FloatField(blank=True, null=True)
    ma20 = models.FloatField(blank=True, null=True)
    ma_v_20 = models.FloatField(blank=True, null=True)
    ma30 = models.FloatField(blank=True, null=True)
    ma_v_30 = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'sync_data_stock_day'
