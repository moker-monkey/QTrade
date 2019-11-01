import datetime
import json
import re
import time

from celery import group, chain, chord
from dateutil import parser
from dateutil.relativedelta import relativedelta

from django_celery_beat.models import CrontabSchedule, PeriodicTask
from QTrade import connect, pro, ts

from .models import SyncRecoder
from .tasks import *
'''
用于启动同步任务的脚本
'''


def test():
    data = ts.pro_bar(
        **{
            'ts_code': '000001.SZ',
            'start_date': '20190801',
            'end_date': '20191030',
            'adj': 'qfq',
            'freq': '5min',
            'ma': [10, 20, 30],
            'factors': ['tor', 'vr']
        })
    print(data)


def init():
    auto_to_sql.delay(
        'disclosure_date',
        '财报披露计划',
        True,
        params={
            'exchage': '',
            'list_status': 'L',
            'fields': 'ts_code,symbol,name,area,industry,list_date'
        })

    # auto_to_sql.delay(
    #     'stock_company',
    #     '上市公司基本信息',
    #     True,
    #     params={
    #         'exchange':
    #         'SSE',
    #         'fields':
    #         'ts_code,chairman,manager,secretary,reg_capital,setup_date,province,city, introduction,main_business,business_scope'
    #     })
    # auto_to_sql.delay(
    #     'stock_company',
    #     '上市公司基本信息',
    #     False,
    #     params={
    #         'exchange':
    #         'SZSE',
    #         'fields':
    #         'ts_code,chairman,manager,secretary,reg_capital,setup_date,province,city, introduction,main_business,business_scope'
    #     })

    # auto_to_sql.delay(
    #     'stock_basic',
    #     '股票列表',
    #     True,
    #     params={
    #         'exchage': '',
    #         'list_status': 'L',
    #         'fields': 'ts_code,symbol,name,area,industry,list_date'
    #     })

    # auto_to_sql.delay(
    #     name='shibor',
    #     describe='上海银行间同业拆放利率',
    #     isCreate='True',
    #     params={
    #         'start_date':'20190801',
    #         'end_date':'20191031'
    #     },
    #     update={
    #         'factor':'-1d'
    #     },
    #     period={
    #         'hour':17
    #     }
    # )

    # auto_to_sql.delay(
    #     name='news',
    #     describe='新闻',
    #     isCreate=True,
    #     params={
    #         'start_date':'20190801',
    #         'end_date':'20191030',
    #         'src':'10jqka'
    #     },
    #     update={
    #         'factor':'-1d'
    #     },
    #     period={
    #         'hour':17
    #     }
    # )

    # loopstock_to_sql.delay(
    #     name='pro_bar',
    #     describe='股票5分钟线',
    #     isCreate=True,
    #     field='ts_code',
    #     alias='stock_5minute',
    #     params={
    #         'start_date': '20190801',
    #         'end_date': '20191030',
    #         'adj': 'qfq',
    #         'freq': '5min',
    #         'ma': [10, 20, 30],
    #         'factors': ['tor', 'vr']
    #     },
    #     update={'factor': '-1d'},
    #     period={'hour':'17'},
    #     wait=12.5)

    # loopstock_to_sql.delay(
    #     name='pro_bar',
    #     describe='股票日线',
    #     isCreate=True,
    #     field='ts_code',
    #     alias='stock_day',
    #     params={
    #         'start_date': '20190801',
    #         'end_date': '20191030',
    #         'adj': 'qfq',
    #         'freq': 'D',
    #         'ma': [10, 20, 30],
    #         'factors': ['tor', 'vr']
    #     },
    #     update={'factor': '-1d'},
    #     period={'hour':'17'},
    #     wait=0)

    # loopstock_to_sql.delay(
    #     name='daily_basic',
    #     describe='每日指标',
    #     isCreate=True,
    #     field='ts_code',
    #     params={
    #         'start_date': '20190801',
    #         'end_date': '20191030',
    #     },
    #     update={
    #         'factor':'-1d',
    #     },
    #     period={'hour':17},
    #     wait=0.4
    # )

    # loopstock_to_sql.delay(
    #     name='express',
    #     describe='业绩快报',
    #     isCreate=True,
    #     field='ts_code',
    #     params={
    #         'start_date': '20190801',
    #         'end_date': '20191101',
    #         'fields':'ts_code,ann_date,end_date,revenue,operate_profit,total_profit,n_income,total_assets,yoy_op,yoy_eps,is_audit,perf_summary'
    #     },
    #     wait=1
    # )


# from sync.tasks_script import init
# init(name='stock_basic',params={'exchage':'','list_status':'L','fields':'ts_code,symbol,name,area,industry,list_date'})