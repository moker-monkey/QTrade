# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class QtdealMycapital(models.Model):
    name = models.CharField(max_length=100)
    capital = models.FloatField()
    money_lock = models.FloatField()
    money_rest = models.FloatField()
    deal_action = models.CharField(max_length=100)
    ts_code = models.CharField(max_length=100)
    deal_price = models.FloatField()
    stock_vol = models.IntegerField()
    profit = models.FloatField(blank=True, null=True)
    profit_rate = models.FloatField(blank=True, null=True)
    bz = models.CharField(max_length=300, blank=True, null=True)
    state_dt = models.CharField(max_length=100)
    hold_days = models.IntegerField(blank=True, null=True)
    serial = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'QTdeal_mycapital'


class QtdealMystockpool(models.Model):
    ts_code = models.CharField(max_length=100)
    buy_price = models.FloatField()
    hold_vol = models.IntegerField()
    hold_days = models.IntegerField()
    opdate = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'QTdeal_mystockpool'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('UsersUserprofile', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoCeleryBeatClockedschedule(models.Model):
    clocked_time = models.DateTimeField()
    enabled = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'django_celery_beat_clockedschedule'


class DjangoCeleryBeatCrontabschedule(models.Model):
    minute = models.CharField(max_length=240)
    hour = models.CharField(max_length=96)
    day_of_week = models.CharField(max_length=64)
    day_of_month = models.CharField(max_length=124)
    month_of_year = models.CharField(max_length=64)
    timezone = models.CharField(max_length=63)

    class Meta:
        managed = False
        db_table = 'django_celery_beat_crontabschedule'


class DjangoCeleryBeatIntervalschedule(models.Model):
    every = models.IntegerField()
    period = models.CharField(max_length=24)

    class Meta:
        managed = False
        db_table = 'django_celery_beat_intervalschedule'


class DjangoCeleryBeatPeriodictask(models.Model):
    name = models.CharField(unique=True, max_length=200)
    task = models.CharField(max_length=200)
    args = models.TextField()
    kwargs = models.TextField()
    queue = models.CharField(max_length=200, blank=True, null=True)
    exchange = models.CharField(max_length=200, blank=True, null=True)
    routing_key = models.CharField(max_length=200, blank=True, null=True)
    expires = models.DateTimeField(blank=True, null=True)
    enabled = models.IntegerField()
    last_run_at = models.DateTimeField(blank=True, null=True)
    total_run_count = models.PositiveIntegerField()
    date_changed = models.DateTimeField()
    description = models.TextField()
    crontab = models.ForeignKey(DjangoCeleryBeatCrontabschedule, models.DO_NOTHING, blank=True, null=True)
    interval = models.ForeignKey(DjangoCeleryBeatIntervalschedule, models.DO_NOTHING, blank=True, null=True)
    solar = models.ForeignKey('DjangoCeleryBeatSolarschedule', models.DO_NOTHING, blank=True, null=True)
    one_off = models.IntegerField()
    start_time = models.DateTimeField(blank=True, null=True)
    priority = models.PositiveIntegerField(blank=True, null=True)
    headers = models.TextField()
    clocked = models.ForeignKey(DjangoCeleryBeatClockedschedule, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_celery_beat_periodictask'


class DjangoCeleryBeatPeriodictasks(models.Model):
    ident = models.SmallIntegerField(primary_key=True)
    last_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_celery_beat_periodictasks'


class DjangoCeleryBeatSolarschedule(models.Model):
    event = models.CharField(max_length=24)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    class Meta:
        managed = False
        db_table = 'django_celery_beat_solarschedule'
        unique_together = (('event', 'latitude', 'longitude'),)


class DjangoCeleryResultsTaskresult(models.Model):
    task_id = models.CharField(unique=True, max_length=255)
    status = models.CharField(max_length=50)
    content_type = models.CharField(max_length=128)
    content_encoding = models.CharField(max_length=64)
    result = models.TextField(blank=True, null=True)
    date_done = models.DateTimeField()
    traceback = models.TextField(blank=True, null=True)
    hidden = models.IntegerField()
    meta = models.TextField(blank=True, null=True)
    task_args = models.TextField(blank=True, null=True)
    task_kwargs = models.TextField(blank=True, null=True)
    task_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_celery_results_taskresult'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class SyncDataDailyBasic(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
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
        managed = False
        db_table = 'sync_data_daily_basic'


class SyncDataDisclosureDate(models.Model):
    ts_code = models.TextField(blank=True, null=True)
    ann_date = models.TextField(blank=True, null=True)
    end_date = models.TextField(blank=True, null=True)
    pre_date = models.TextField(blank=True, null=True)
    actual_date = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sync_data_disclosure_date'


class SyncDataDividend(models.Model):
    ts_code = models.TextField(blank=True, null=True)
    trade_date = models.TextField(blank=True, null=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    pre_close = models.FloatField(blank=True, null=True)
    change = models.FloatField(blank=True, null=True)
    pct_chg = models.FloatField(blank=True, null=True)
    vol = models.FloatField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sync_data_dividend'


class SyncDataExpress(models.Model):
    ts_code = models.TextField(blank=True, null=True)
    ann_date = models.TextField(blank=True, null=True)
    end_date = models.TextField(blank=True, null=True)
    revenue = models.TextField(blank=True, null=True)
    operate_profit = models.TextField(blank=True, null=True)
    total_profit = models.TextField(blank=True, null=True)
    n_income = models.TextField(blank=True, null=True)
    total_assets = models.TextField(blank=True, null=True)
    yoy_op = models.TextField(blank=True, null=True)
    yoy_eps = models.TextField(blank=True, null=True)
    perf_summary = models.TextField(blank=True, null=True)
    is_audit = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sync_data_express'


class SyncDataFinaIndicator(models.Model):
    ts_code = models.TextField(blank=True, null=True)
    ann_date = models.TextField(blank=True, null=True)
    end_date = models.TextField(blank=True, null=True)
    eps = models.FloatField(blank=True, null=True)
    dt_eps = models.FloatField(blank=True, null=True)
    total_revenue_ps = models.FloatField(blank=True, null=True)
    revenue_ps = models.FloatField(blank=True, null=True)
    capital_rese_ps = models.FloatField(blank=True, null=True)
    surplus_rese_ps = models.FloatField(blank=True, null=True)
    undist_profit_ps = models.FloatField(blank=True, null=True)
    extra_item = models.FloatField(blank=True, null=True)
    profit_dedt = models.FloatField(blank=True, null=True)
    gross_margin = models.TextField(blank=True, null=True)
    current_ratio = models.FloatField(blank=True, null=True)
    quick_ratio = models.FloatField(blank=True, null=True)
    cash_ratio = models.TextField(blank=True, null=True)
    ar_turn = models.TextField(blank=True, null=True)
    ca_turn = models.TextField(blank=True, null=True)
    fa_turn = models.FloatField(blank=True, null=True)
    assets_turn = models.FloatField(blank=True, null=True)
    op_income = models.FloatField(blank=True, null=True)
    ebit = models.TextField(blank=True, null=True)
    ebitda = models.TextField(blank=True, null=True)
    fcff = models.FloatField(blank=True, null=True)
    fcfe = models.TextField(blank=True, null=True)
    current_exint = models.TextField(blank=True, null=True)
    noncurrent_exint = models.TextField(blank=True, null=True)
    interestdebt = models.TextField(blank=True, null=True)
    netdebt = models.TextField(blank=True, null=True)
    tangible_asset = models.TextField(blank=True, null=True)
    working_capital = models.TextField(blank=True, null=True)
    networking_capital = models.TextField(blank=True, null=True)
    invest_capital = models.TextField(blank=True, null=True)
    retained_earnings = models.FloatField(blank=True, null=True)
    diluted2_eps = models.FloatField(blank=True, null=True)
    bps = models.FloatField(blank=True, null=True)
    ocfps = models.FloatField(blank=True, null=True)
    retainedps = models.FloatField(blank=True, null=True)
    cfps = models.FloatField(blank=True, null=True)
    ebit_ps = models.TextField(blank=True, null=True)
    fcff_ps = models.TextField(blank=True, null=True)
    fcfe_ps = models.TextField(blank=True, null=True)
    netprofit_margin = models.FloatField(blank=True, null=True)
    grossprofit_margin = models.TextField(blank=True, null=True)
    cogs_of_sales = models.TextField(blank=True, null=True)
    expense_of_sales = models.TextField(blank=True, null=True)
    profit_to_gr = models.FloatField(blank=True, null=True)
    saleexp_to_gr = models.TextField(blank=True, null=True)
    adminexp_of_gr = models.FloatField(blank=True, null=True)
    finaexp_of_gr = models.TextField(blank=True, null=True)
    impai_ttm = models.FloatField(blank=True, null=True)
    gc_of_gr = models.TextField(blank=True, null=True)
    op_of_gr = models.FloatField(blank=True, null=True)
    ebit_of_gr = models.TextField(blank=True, null=True)
    roe = models.FloatField(blank=True, null=True)
    roe_waa = models.FloatField(blank=True, null=True)
    roe_dt = models.FloatField(blank=True, null=True)
    roa = models.TextField(blank=True, null=True)
    npta = models.FloatField(blank=True, null=True)
    roic = models.TextField(blank=True, null=True)
    roe_yearly = models.FloatField(blank=True, null=True)
    roa2_yearly = models.TextField(blank=True, null=True)
    debt_to_assets = models.FloatField(blank=True, null=True)
    assets_to_eqt = models.FloatField(blank=True, null=True)
    dp_assets_to_eqt = models.FloatField(blank=True, null=True)
    ca_to_assets = models.TextField(blank=True, null=True)
    nca_to_assets = models.TextField(blank=True, null=True)
    tbassets_to_totalassets = models.TextField(blank=True, null=True)
    int_to_talcap = models.TextField(blank=True, null=True)
    eqt_to_talcapital = models.TextField(blank=True, null=True)
    currentdebt_to_debt = models.TextField(blank=True, null=True)
    longdeb_to_debt = models.TextField(blank=True, null=True)
    ocf_to_shortdebt = models.TextField(blank=True, null=True)
    debt_to_eqt = models.FloatField(blank=True, null=True)
    eqt_to_debt = models.FloatField(blank=True, null=True)
    eqt_to_interestdebt = models.TextField(blank=True, null=True)
    tangibleasset_to_debt = models.TextField(blank=True, null=True)
    tangasset_to_intdebt = models.TextField(blank=True, null=True)
    tangibleasset_to_netdebt = models.TextField(blank=True, null=True)
    ocf_to_debt = models.FloatField(blank=True, null=True)
    turn_days = models.TextField(blank=True, null=True)
    roa_yearly = models.FloatField(blank=True, null=True)
    roa_dp = models.FloatField(blank=True, null=True)
    fixed_assets = models.FloatField(blank=True, null=True)
    profit_to_op = models.FloatField(blank=True, null=True)
    q_saleexp_to_gr = models.TextField(blank=True, null=True)
    q_gc_to_gr = models.TextField(blank=True, null=True)
    q_roe = models.FloatField(blank=True, null=True)
    q_dt_roe = models.FloatField(blank=True, null=True)
    q_npta = models.FloatField(blank=True, null=True)
    q_ocf_to_sales = models.FloatField(blank=True, null=True)
    basic_eps_yoy = models.FloatField(blank=True, null=True)
    dt_eps_yoy = models.FloatField(blank=True, null=True)
    cfps_yoy = models.FloatField(blank=True, null=True)
    op_yoy = models.FloatField(blank=True, null=True)
    ebt_yoy = models.FloatField(blank=True, null=True)
    netprofit_yoy = models.FloatField(blank=True, null=True)
    dt_netprofit_yoy = models.FloatField(blank=True, null=True)
    ocf_yoy = models.FloatField(blank=True, null=True)
    roe_yoy = models.FloatField(blank=True, null=True)
    bps_yoy = models.FloatField(blank=True, null=True)
    assets_yoy = models.FloatField(blank=True, null=True)
    eqt_yoy = models.FloatField(blank=True, null=True)
    tr_yoy = models.FloatField(blank=True, null=True)
    or_yoy = models.FloatField(blank=True, null=True)
    q_sales_yoy = models.FloatField(blank=True, null=True)
    q_op_qoq = models.FloatField(blank=True, null=True)
    equity_yoy = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sync_data_fina_indicator'


class SyncDataNews(models.Model):
    datetime = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    title = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'sync_data_news'


class SyncDataShibor(models.Model):
    date = models.TextField()
    on = models.FloatField(blank=True, null=True)
    number_1w = models.FloatField(db_column='1w', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2w = models.FloatField(db_column='2w', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1m = models.FloatField(db_column='1m', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3m = models.FloatField(db_column='3m', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_6m = models.FloatField(db_column='6m', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_9m = models.FloatField(db_column='9m', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1y = models.FloatField(db_column='1y', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'sync_data_shibor'


class SyncDataStock5Minute(models.Model):
    ts_code = models.TextField(blank=True, null=True)
    trade_time = models.TextField(blank=True, null=True)
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
        managed = False
        db_table = 'sync_data_stock_5minute'


class SyncDataStockBasic(models.Model):
    ts_code = models.TextField(blank=True, null=True)
    symbol = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    area = models.TextField(blank=True, null=True)
    industry = models.TextField(blank=True, null=True)
    list_date = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sync_data_stock_basic'


class SyncDataStockCompany(models.Model):
    ts_code = models.TextField(blank=True, null=True)
    chairman = models.TextField(blank=True, null=True)
    manager = models.TextField(blank=True, null=True)
    secretary = models.TextField(blank=True, null=True)
    reg_capital = models.FloatField(blank=True, null=True)
    setup_date = models.TextField(blank=True, null=True)
    province = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    introduction = models.TextField(blank=True, null=True)
    business_scope = models.TextField(blank=True, null=True)
    main_business = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sync_data_stock_company'


class SyncDataStockDay(models.Model):
    trade_date = models.TextField(blank=True, null=True)
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
        managed = False
        db_table = 'sync_data_stock_day'


class SyncSyncrecoder(models.Model):
    name = models.CharField(max_length=30)
    alias = models.CharField(unique=True, max_length=30)
    describe = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=30)
    update_time = models.DateTimeField()
    create_time = models.DateTimeField()
    rate = models.CharField(max_length=30)
    task = models.CharField(max_length=30)
    params = models.CharField(max_length=1000, blank=True, null=True)
    update = models.CharField(max_length=1000, blank=True, null=True)
    period = models.CharField(max_length=100)
    error = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sync_syncrecoder'


class UsersUserprofile(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    name = models.CharField(max_length=30, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    mobile = models.CharField(max_length=11, blank=True, null=True)
    gender = models.CharField(max_length=6)
    email = models.CharField(max_length=100, blank=True, null=True)
    cash = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'users_userprofile'


class UsersUserprofileGroups(models.Model):
    userprofile = models.ForeignKey(UsersUserprofile, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users_userprofile_groups'
        unique_together = (('userprofile', 'group'),)


class UsersUserprofileStock(models.Model):
    userprofile = models.ForeignKey(UsersUserprofile, models.DO_NOTHING)
    syncdatastockbasic_id = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'users_userprofile_stock'


class UsersUserprofileUserPermissions(models.Model):
    userprofile = models.ForeignKey(UsersUserprofile, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users_userprofile_user_permissions'
        unique_together = (('userprofile', 'permission'),)
