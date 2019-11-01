# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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


class SyncDataNews(models.Model):
    datetime = models.TextField(blank=True, null=True)
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


class UsersUserprofileUserPermissions(models.Model):
    userprofile = models.ForeignKey(UsersUserprofile, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users_userprofile_user_permissions'
        unique_together = (('userprofile', 'permission'),)
