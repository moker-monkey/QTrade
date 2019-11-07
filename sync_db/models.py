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
    trade_date = models.CharField(max_length=100, verbose_name='交易日')
    close = models.FloatField(blank=True, null=True, verbose_name='当日收盘价')
    turnover_rate = models.FloatField(
        blank=True, null=True, verbose_name='换手率(%)')
    turnover_rate_f = models.FloatField(
        blank=True, null=True, verbose_name='换手率(自由流通股)')
    volume_ratio = models.FloatField(blank=True, null=True, verbose_name='量比')
    pe = models.FloatField(blank=True, null=True, verbose_name='市盈率(总市值/净利润)')
    pe_ttm = models.FloatField(blank=True, null=True, verbose_name='市盈率(TTM)')
    pb = models.FloatField(blank=True, null=True, verbose_name='市净率(总市值/净资产)')
    ps = models.FloatField(blank=True, null=True, verbose_name='市销率')
    ps_ttm = models.FloatField(blank=True, null=True, verbose_name='市销率(TTM)')
    total_share = models.FloatField(
        blank=True, null=True, verbose_name='总股本(万股)')
    float_share = models.FloatField(
        blank=True, null=True, verbose_name='流通股本(万股)')
    free_share = models.FloatField(
        blank=True, null=True, verbose_name='自由流通股本(万)')
    total_mv = models.FloatField(blank=True, null=True, verbose_name='总市值(万元)')
    circ_mv = models.FloatField(blank=True, null=True, verbose_name='流通市值(万元)')

    class Meta:
        db_table = 'sync_data_daily_basic'


class SyncDataNews(models.Model):
    datetime = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    title = models.CharField(
        primary_key=True, default='000000', max_length=200)

    class Meta:
        db_table = 'sync_data_news'


class SyncDataShibor(models.Model):
    date = models.CharField(
        primary_key=True,
        default='00000000',
        max_length=100,
        verbose_name='日期')
    on = models.FloatField(blank=True, null=True, verbose_name='隔夜')
    number_1w = models.FloatField(
        db_column='1w', blank=True, null=True, verbose_name='1周'
    )  # Field renamed because it wasn't a valid Python identifier.
    number_2w = models.FloatField(
        db_column='2w', blank=True, null=True, verbose_name='2周'
    )  # Field renamed because it wasn't a valid Python identifier.
    number_1m = models.FloatField(
        db_column='1m', blank=True, null=True, verbose_name='1个月'
    )  # Field renamed because it wasn't a valid Python identifier.
    number_3m = models.FloatField(
        db_column='3m', blank=True, null=True, verbose_name='3个月'
    )  # Field renamed because it wasn't a valid Python identifier.
    number_6m = models.FloatField(
        db_column='6m', blank=True, null=True, verbose_name='6个月'
    )  # Field renamed because it wasn't a valid Python identifier.
    number_9m = models.FloatField(
        db_column='9m', blank=True, null=True, verbose_name='9个月'
    )  # Field renamed because it wasn't a valid Python identifier.
    number_1y = models.FloatField(
        db_column='1y', blank=True, null=True, verbose_name='一年'
    )  # Field renamed because it wasn't a valid Python identifier.

    class Meta:
        db_table = 'sync_data_shibor'


class SyncDataStock5Minute(models.Model):
    ts_code = models.TextField(blank=True, null=True, verbose_name='股票代码')
    trade_time = models.CharField(
        primary_key=True,
        default='000000',
        max_length=100,
        verbose_name='交易时间')
    open = models.FloatField(blank=True, null=True, verbose_name='开盘价')
    close = models.FloatField(blank=True, null=True, verbose_name='收盘价')
    high = models.FloatField(blank=True, null=True, verbose_name='最高价')
    low = models.FloatField(blank=True, null=True, verbose_name='最低价')
    vol = models.FloatField(blank=True, null=True, verbose_name='成交量(手)')
    amount = models.FloatField(blank=True, null=True, verbose_name='成交额(千元)')
    ma10 = models.FloatField(blank=True, null=True, verbose_name='10均线')
    ma_v_10 = models.FloatField(blank=True, null=True, verbose_name='')
    ma20 = models.FloatField(blank=True, null=True, verbose_name='20均线')
    ma_v_20 = models.FloatField(blank=True, null=True, verbose_name='')
    ma30 = models.FloatField(blank=True, null=True, verbose_name='30均线')
    ma_v_30 = models.FloatField(blank=True, null=True, verbose_name='')

    class Meta:
        db_table = 'sync_data_stock_5minute'


class SyncDataStockBasic(models.Model):
    ts_code = models.CharField(
        primary_key=True, default='000000', max_length=100)
    symbol = models.TextField(blank=True, null=True, verbose_name='股票代码')
    name = models.TextField(blank=True, null=True, verbose_name='股票名称')
    area = models.TextField(blank=True, null=True, verbose_name='所在区域')
    industry = models.TextField(blank=True, null=True, verbose_name='所属行业')
    list_date = models.TextField(blank=True, null=True, verbose_name='上市日期')

    class Meta:
        db_table = 'sync_data_stock_basic'


class SyncDataStockDay(models.Model):
    trade_date = models.CharField(
        primary_key=True,
        default='000000',
        max_length=100,
        verbose_name='交易日期')
    ts_code = models.TextField(blank=True, null=True, verbose_name='TS')
    open = models.FloatField(blank=True, null=True, verbose_name='开盘价')
    high = models.FloatField(blank=True, null=True, verbose_name='最高价')
    low = models.FloatField(blank=True, null=True, verbose_name='最低价')
    close = models.FloatField(blank=True, null=True, verbose_name='收盘价')
    pre_close = models.FloatField(blank=True, null=True, verbose_name='昨收')
    change = models.FloatField(blank=True, null=True, verbose_name='涨跌额')
    pct_chg = models.FloatField(blank=True, null=True, verbose_name='涨跌幅(前复权)')
    vol = models.FloatField(blank=True, null=True, verbose_name='成交量(手)')
    amount = models.FloatField(blank=True, null=True, verbose_name='成交额(千元)')
    turnover_rate = models.FloatField(
        blank=True, null=True, verbose_name='换手率')
    volume_ratio = models.FloatField(blank=True, null=True, verbose_name='量比')
    ma10 = models.FloatField(blank=True, null=True, verbose_name='10日均线')
    ma_v_10 = models.FloatField(blank=True, null=True, verbose_name='10日均线复权')
    ma20 = models.FloatField(blank=True, null=True, verbose_name='20日均线')
    ma_v_20 = models.FloatField(blank=True, null=True, verbose_name='20日均线复权')
    ma30 = models.FloatField(blank=True, null=True, verbose_name='30日均线')
    ma_v_30 = models.FloatField(blank=True, null=True, verbose_name='30日均线复权')

    class Meta:
        db_table = 'sync_data_stock_day'


#===================== 基本面models =======================

class SyncDataDisclosureDate(models.Model):
    id = models.AutoField(primary_key=True)
    ts_code = models.TextField(blank=True, null=True, verbose_name='TS')
    ann_date = models.TextField(blank=True, null=True, verbose_name='最新披露公告日')
    end_date = models.TextField(blank=True, null=True, verbose_name='季度周期')
    pre_date = models.TextField(blank=True, null=True, verbose_name='预计披露日期')
    actual_date = models.TextField(
        blank=True, null=True, verbose_name='实际披露日期')

    class Meta:
        db_table = 'sync_data_disclosure_date'


class SyncDataExpress(models.Model):
    id = models.AutoField(primary_key=True)
    ts_code = models.TextField(blank=True, null=True, verbose_name='TS')
    ann_date = models.TextField(blank=True, null=True, verbose_name='公告日期')
    end_date = models.TextField(blank=True, null=True, verbose_name='报告期')
    revenue = models.TextField(blank=True, null=True, verbose_name='营业收入(元)')
    operate_profit = models.TextField(
        blank=True, null=True, verbose_name='营业利润(元)')
    total_profit = models.TextField(
        blank=True, null=True, verbose_name='利润总额(元)')
    n_income = models.TextField(blank=True, null=True, verbose_name='净利润(元)')
    total_assets = models.TextField(
        blank=True, null=True, verbose_name='总资产(元)')
    yoy_op = models.TextField(blank=True, null=True, verbose_name='同比增长率:营业利润')
    yoy_eps = models.TextField(
        blank=True, null=True, verbose_name='同比增长率:基本每股收益')
    perf_summary = models.TextField(
        blank=True, null=True, verbose_name='业绩简要说明')
    is_audit = models.TextField(blank=True, null=True, verbose_name='是否审计')

    class Meta:
        db_table = 'sync_data_express'


class SyncDataFinaIndicator(models.Model):
    id = models.AutoField(primary_key=True)
    ts_code = models.TextField(blank=True, null=True, verbose_name='TS')
    ann_date = models.TextField(blank=True, null=True, verbose_name='公告日期')
    end_date = models.TextField(blank=True, null=True, verbose_name='报告期')
    eps = models.FloatField(blank=True, null=True, verbose_name='基本每股收益率')
    dt_eps = models.FloatField(blank=True, null=True, verbose_name='稀释每股收益')
    total_revenue_ps = models.FloatField(
        blank=True, null=True, verbose_name='每股营业总收入')
    revenue_ps = models.FloatField(
        blank=True, null=True, verbose_name='每股营业收入')
    capital_rese_ps = models.FloatField(
        blank=True, null=True, verbose_name='每股资本公积')
    surplus_rese_ps = models.FloatField(
        blank=True, null=True, verbose_name='每股盈余公积')
    undist_profit_ps = models.FloatField(
        blank=True, null=True, verbose_name='每股未分配利润')
    extra_item = models.FloatField(
        blank=True, null=True, verbose_name='非经常性损益')
    profit_dedt = models.FloatField(
        blank=True, null=True, verbose_name='扣除非经常性损益后的净利润')
    gross_margin = models.TextField(blank=True, null=True, verbose_name='毛利')
    current_ratio = models.FloatField(
        blank=True, null=True, verbose_name='流动比率')
    quick_ratio = models.FloatField(blank=True, null=True, verbose_name='速动比率')
    cash_ratio = models.TextField(blank=True, null=True, verbose_name='保守速动比率')
    ar_turn = models.TextField(blank=True, null=True, verbose_name='应收帐款周转率')
    ca_turn = models.TextField(blank=True, null=True, verbose_name='流动资产周转率')
    fa_turn = models.FloatField(blank=True, null=True, verbose_name='固定支持周转率')
    assets_turn = models.FloatField(
        blank=True, null=True, verbose_name='总资产周转率')
    op_income = models.FloatField(
        blank=True, null=True, verbose_name='经营活动净收益')
    ebit = models.TextField(blank=True, null=True, verbose_name='息税前利润')
    ebitda = models.TextField(blank=True, null=True, verbose_name='息税折旧摊销前利润')
    fcff = models.FloatField(blank=True, null=True, verbose_name='企业自由现金流量')
    fcfe = models.TextField(blank=True, null=True, verbose_name='股权自由现金流量')
    current_exint = models.TextField(
        blank=True, null=True, verbose_name='无息流动负债')
    noncurrent_exint = models.TextField(
        blank=True, null=True, verbose_name='无息非流动负债')
    interestdebt = models.TextField(blank=True, null=True, verbose_name='带息负债')
    netdebt = models.TextField(blank=True, null=True, verbose_name='净负债')
    tangible_asset = models.TextField(
        blank=True, null=True, verbose_name='有形资产')
    working_capital = models.TextField(
        blank=True, null=True, verbose_name='运营资金')
    networking_capital = models.TextField(
        blank=True, null=True, verbose_name='运营流动资本')
    invest_capital = models.TextField(
        blank=True, null=True, verbose_name='全部投入资本')
    retained_earnings = models.FloatField(
        blank=True, null=True, verbose_name='留存收益')
    diluted2_eps = models.FloatField(
        blank=True, null=True, verbose_name='期末摊薄每股收益')
    bps = models.FloatField(blank=True, null=True, verbose_name='每股净资产')
    ocfps = models.FloatField(
        blank=True, null=True, verbose_name='每股经营活动产生的现金流量净额')
    retainedps = models.FloatField(
        blank=True, null=True, verbose_name='每股留存收益')
    cfps = models.FloatField(blank=True, null=True, verbose_name='每股现金流量净额')
    ebit_ps = models.TextField(blank=True, null=True, verbose_name='每股息税前利润')
    fcff_ps = models.TextField(
        blank=True, null=True, verbose_name='每股企业自由现金流量')
    fcfe_ps = models.TextField(
        blank=True, null=True, verbose_name='每股股东自由现金流量')
    netprofit_margin = models.FloatField(
        blank=True, null=True, verbose_name='销售净利率')
    grossprofit_margin = models.TextField(
        blank=True, null=True, verbose_name='销售毛利率')
    cogs_of_sales = models.TextField(
        blank=True, null=True, verbose_name='销售成本率')
    expense_of_sales = models.TextField(
        blank=True, null=True, verbose_name='销售期间费用率')
    profit_to_gr = models.FloatField(
        blank=True, null=True, verbose_name='净利润/营业总收入')
    saleexp_to_gr = models.TextField(
        blank=True, null=True, verbose_name='销售费用/营业总收入')
    adminexp_of_gr = models.FloatField(
        blank=True, null=True, verbose_name='管理费用/营业总收入')
    finaexp_of_gr = models.TextField(
        blank=True, null=True, verbose_name='财富费用/营业总收入')
    impai_ttm = models.FloatField(
        blank=True, null=True, verbose_name='资产减值损失/营业总收入')
    gc_of_gr = models.TextField(
        blank=True, null=True, verbose_name='营业总成本/营业总收入')
    op_of_gr = models.FloatField(
        blank=True, null=True, verbose_name='营业利润/营业总收入')
    ebit_of_gr = models.TextField(
        blank=True, null=True, verbose_name='息税前利润/营业总收入')
    roe = models.FloatField(blank=True, null=True, verbose_name='净资产收益率')
    roe_waa = models.FloatField(
        blank=True, null=True, verbose_name='加权平均净资产收益率')
    roe_dt = models.FloatField(
        blank=True, null=True, verbose_name='净资产收益率(扣除非经常损益)')
    roa = models.TextField(blank=True, null=True, verbose_name='总资产报酬率')
    npta = models.FloatField(blank=True, null=True, verbose_name='总资产净利润')
    roic = models.TextField(blank=True, null=True, verbose_name='投入资本回报率')
    roe_yearly = models.FloatField(
        blank=True, null=True, verbose_name='年化净资产收益率')
    roa2_yearly = models.TextField(
        blank=True, null=True, verbose_name='年化总资产报酬率')
    debt_to_assets = models.FloatField(
        blank=True, null=True, verbose_name='资产负债率')
    assets_to_eqt = models.FloatField(
        blank=True, null=True, verbose_name='权益乘数')
    dp_assets_to_eqt = models.FloatField(
        blank=True, null=True, verbose_name='权益乘数(杜邦分析)')
    ca_to_assets = models.TextField(
        blank=True, null=True, verbose_name='流动资产/总资产')
    nca_to_assets = models.TextField(
        blank=True, null=True, verbose_name='非流动资产/总资产')
    tbassets_to_totalassets = models.TextField(
        blank=True, null=True, verbose_name='有形资产/总资产')
    int_to_talcap = models.TextField(
        blank=True, null=True, verbose_name='带息债务/全部投入资本')
    eqt_to_talcapital = models.TextField(
        blank=True, null=True, verbose_name='归属于母公司的股东权益/全部投入资本')
    currentdebt_to_debt = models.TextField(
        blank=True, null=True, verbose_name='流动负债/负债合计')
    longdeb_to_debt = models.TextField(
        blank=True, null=True, verbose_name='非流动负债/负债合计')
    ocf_to_shortdebt = models.TextField(
        blank=True, null=True, verbose_name='经营活动产生的现金流量净额/流动负债')
    debt_to_eqt = models.FloatField(blank=True, null=True, verbose_name='产权比率')
    eqt_to_debt = models.FloatField(
        blank=True, null=True, verbose_name='归属于母公司的股东权益/负债合计')
    eqt_to_interestdebt = models.TextField(
        blank=True, null=True, verbose_name='归属于母公司的股东权益/带息负债')
    tangibleasset_to_debt = models.TextField(
        blank=True, null=True, verbose_name='有形资产/负债合计')
    tangasset_to_intdebt = models.TextField(
        blank=True, null=True, verbose_name='有形资产/带息债务')
    tangibleasset_to_netdebt = models.TextField(
        blank=True, null=True, verbose_name='有形资产/净债务')
    ocf_to_debt = models.FloatField(
        blank=True, null=True, verbose_name='经营活动产生的现金流量净额/负债合计')
    turn_days = models.TextField(blank=True, null=True, verbose_name='营业周期')
    roa_yearly = models.FloatField(
        blank=True, null=True, verbose_name='年化总资产净利润')
    roa_dp = models.FloatField(
        blank=True, null=True, verbose_name='总资产净利润(杜邦分析)')
    fixed_assets = models.FloatField(
        blank=True, null=True, verbose_name='固定资产合计')
    profit_to_op = models.FloatField(
        blank=True, null=True, verbose_name='利润总额/营业收入')
    q_saleexp_to_gr = models.TextField(
        blank=True, null=True, verbose_name='销售费用/营业总收入')
    q_gc_to_gr = models.TextField(
        blank=True, null=True, verbose_name='营业总成本/营业总收入(单季度)')
    q_roe = models.FloatField(
        blank=True, null=True, verbose_name='净资产收益率(单季度)')
    q_dt_roe = models.FloatField(
        blank=True, null=True, verbose_name='净资产单季度收益率(扣除非经常损益)')
    q_npta = models.FloatField(
        blank=True, null=True, verbose_name='总资产净利润(单季度)')
    q_ocf_to_sales = models.FloatField(
        blank=True, null=True, verbose_name='经营活动产生的现金流量净额/营业收入(单季度)')
    basic_eps_yoy = models.FloatField(
        blank=True, null=True, verbose_name='基本每股收益同比增长率(%)')
    dt_eps_yoy = models.FloatField(
        blank=True, null=True, verbose_name='稀释每股收益同比增长率(%)')
    cfps_yoy = models.FloatField(
        blank=True, null=True, verbose_name='每股经营活动产生的现金流量净额同比增长率(%)')
    op_yoy = models.FloatField(
        blank=True, null=True, verbose_name='营业利润同比增长率(%)')
    ebt_yoy = models.FloatField(
        blank=True, null=True, verbose_name='利润总额同比增长率(%)')
    netprofit_yoy = models.FloatField(
        blank=True, null=True, verbose_name='归属母公司股东的净利润同比增长率(%)')
    dt_netprofit_yoy = models.FloatField(
        blank=True, null=True, verbose_name='归属母公司股东的净利润-扣除非经常损益同比增长率')
    ocf_yoy = models.FloatField(
        blank=True, null=True, verbose_name='经营活动产生的现金流量净额同比增长率(%)')
    roe_yoy = models.FloatField(
        blank=True, null=True, verbose_name='净资产收益率(摊薄)同比增长率(%)')
    bps_yoy = models.FloatField(
        blank=True, null=True, verbose_name='每股净资产相对年初增长率(%)')
    assets_yoy = models.FloatField(
        blank=True, null=True, verbose_name='资产总计相对年初增长率(%)')
    eqt_yoy = models.FloatField(
        blank=True, null=True, verbose_name='归属母公司的股东权益相对年初增长率(%)')
    tr_yoy = models.FloatField(
        blank=True, null=True, verbose_name='营业总收入同比增长率(%)')
    or_yoy = models.FloatField(
        blank=True, null=True, verbose_name='营业收入同比增长率(%)')
    q_sales_yoy = models.FloatField(
        blank=True, null=True, verbose_name='营业收入环比增长率(%)(单季度)')
    q_op_qoq = models.FloatField(
        blank=True, null=True, verbose_name='营业利润同比增长率(%)(单季度)')
    equity_yoy = models.FloatField(
        blank=True, null=True, verbose_name='净资产同比增长率')

    class Meta:
        db_table = 'sync_data_fina_indicator'