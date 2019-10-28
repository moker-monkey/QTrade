# from __future__ import absolute_import, unicode_literals
import datetime
import json
import re
import time

from celery import shared_task
from dateutil import parser
from dateutil.relativedelta import relativedelta

from django_celery_beat.models import CrontabSchedule, PeriodicTask
from QTrade import connect, pro, ts

from .models import SyncRecoder
from sync_db.models import SyncDataStockBasic


@shared_task(bind=True)
def tushare_to_sql(self,
                   name,
                   describe,
                   isCreate,
                   alias='',
                   period={},
                   update={},
                   **kwargs):
    '''
    获取tushare数据
    name：能够生成table名字，以‘sync_data_'+name命名
          同时也是tushare的api
          和Recoder中的name
    alias: 用于在name相同的情况下区分数据库
    kw：tushare的参数
    period：tushare同步周期
    describe：api的描述
    isCreate：是否第一次执行
    每执行一次，就会记录在SyncRecoder中对应name中
    如果执行报错也会记录更新时间，但是status为失败
    update：用于更新的参数，会与params合并
        如果传factor，就会安装factor去计算参数的周期，如果没传，默认是上次更新时间，到今天的数据
    '''
    status = ''
    inner_name = alias if alias else name
    try:
        if not isCreate:
            # 计算更新参数，其中start_time是指向当前时间
            record = SyncRecoder.objects.get(name=inner_name)
            start_time = datetime.datetime.now()
            factor = record.get('update').get('factor')
            if factor:
                end_time = handleFactorDate(start_time, factor)
            else:
                end_time = record.get('update_time') + datetime.timedelta(
                    days=1)
            if re.match(r'-', factor):
                # +1天是因为同步数据是包括头和尾的数据
                end_time = end_time + datetime.timedelta(days=1)
            kwargs['start_date'] = start_time.strftime('%Y%m%d')
            kwargs['end_date'] = end_time.strftime('%Y%m%d')
            if kwargs.get('trade_date'):
                # 如果是同一天，则使用‘trade_date’参数
                kwargs['trade_date'] = start_time.strftime('%Y%m%d')
                del kwargs['start_date']
                del kwargs['end_date']
        if name == 'shibor':
            data = pro.shibor(**kwargs)
        elif alias:
            data = ts.pro_bar(**kwargs)
        else:
            data = pro.query(name, **kwargs)

        status = 'success'
        # 初次获取数据后就将该任务加为周期任务
        if not isCreate:
            SyncRecoder.objects.update_or_create(
                name=inner_name, defaults={
                    'status': status,
                    'error': '',
                })
        else:

            if period:
                schedule, _ = CrontabSchedule.objects.get_or_create(**period)
                PeriodicTask.objects.update_or_create(
                    name=f'sync_{inner_name}',
                    defaults={
                        'crontab':
                        schedule,
                        'task':
                        self.name,
                        'kwargs':
                        json.dumps(kwargs.update(update)),
                        'args':
                        json.dumps([
                            inner_name,
                            json.dumps(period), describe, False, alias
                        ])
                    })

    except Exception as e:
        status = 'failure'
        SyncRecoder.objects.update_or_create(
            name=inner_name, defaults={
                'status': status,
                'error': e
            })
        print(e)
    finally:
        return {
            'detail': {
                'name': inner_name,
                'status': status,
                'task': self.name,
                'time': datetime.datetime.now()
            }
        }


def handleFactorDate(start_time, factor):
    '''
    start_time: 是一个datetime对象
    factor：类似-5d，5d，1m
    由于是同步功能，更新时都表示之前的数据已经更新完成，
    更新表示获取从上次更新时间到现在的数据
    该函数用于处理参数中的时间，在更新时使用的参数
    '''
    startTime = start_time if start_time else datetime.datetime.now()
    rex = re.match(r'(-?)(\d)(\w){1}', factor)
    if rex.group(3) == 'd':
        end_time = f'startTime{"-" if rex.group(1) else "+"}datetime.timedelta(days={rex.group(2)})'
    elif rex.group(3) == 'm':
        end_time = f'startTime{"-" if rex.group(1) else "+"}relativedelta(months={rex.group(2)})'
    elif rex.group(3) == 'y':
        end_time = f'startTime{"-" if rex.group(1) else "+"}relativedelta(years={rex.group(2)})'
    return eval(end_time)


@shared_task(bind=True)
def LoopSync(self,
             name,
             describe,
             isCreate,
             source,
             field,
             rate,
             alias='',
             period={},
             update={},
             **kwargs):
    '''
    用于需要根据列表去取值的api
    '''
    for inx, val in enumerate(source):
        tushare_to_sql.delay(
            name=name,
            describe=describe,
            isCreate=False,
            alias=alias,
            **kwargs)
        print(f'total:{len(source)}/current{inx+1}')


def init_sync(init_type):
    '''
    init_type: period | once | all 表示执行（周期|一次性|全部）的数据同步
    '''
    if init_type == 'first':
        # first 任务是前置任务，在once任务中所需要的
        # 执行后需要手动反向生成model
        tushare_to_sql.delay(
            name='stock_basic',
            describe='股票列表',
            isCreate=True,
            **{
                'exchange': '',
                'list_status': 'L',
                'fields': 'ts_code,symbol,name,area,industry,list_date'
            })

    if init_type == 'period' or init_type == 'all':
        tushare_to_sql.delay(
            name='trade_cal',
            describe='交易日历',
            period={'month_of_year': 1},
            isCreate=True,
            update={
                'factor': '1y',
            },
            **{
                'exchange': '',
                'start_date': '20191015',
                'end_date': '20191231'
            })

        tushare_to_sql.delay(
            name='pro_bar',
            alias='stock_day',
            describe='日线股票',
            period={'hour': 16},
            isCreate=True,
            update={
                'factor': '-1d',
            },
            **{
                'start_date': '20190801',
                'end_date': '20191023'
            })

        tushare_to_sql.delay(
            name='shibor',
            describe='上海同业拆借利率',
            period={'hour': 12},
            isCreate=True,
            update={'factor': '-1d'},
            **{
                'start_date': '20190801',
                'end_date': '20191023',
            })
    if init_type == 'once' or init_type == 'all':
        stockList = SyncDataStockBasic.objects.all()
        for inx, val in enumerate(stockList):
            tushare_to_sql.delay(
                name='pro_bar',
                alias='stock_min',
                describe='分钟股票',
                isCreate=True if not inx else False,
                **{
                    'ts_code': val.ts_code,
                    'start_date': '20190801',
                    'trade_date': '20191028',
                    'freq': '1min',
                    'adj': 'qfq',
                    'ma': [10, 20, 30],
                    'factors': ['tor', 'vr']
                })
            progressText(len(stockList),inx+1,'分钟股票')
            time.sleep(2)

        # tushare_to_sql.delay(
        #     name='daily_basic',
        #     describe='每日指标',
        #     period={'hour': 16},
        #     isCreate=True,
        #     update={'factor': '-1d',
        #             'trade_date': True},
        #     **{
        #         'start_date': '20190801',
        #         'end_date': '20191023',
        #     })

def progressText(total,current,name=''):
    print(f'当前执行{name},进度{current}/{total}')

from cgi import parse
