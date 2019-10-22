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


@shared_task(bind=True)
def tushare_to_sql(self, name, period, describe, isCreate, update={},table_name='',
                   **kwargs):
    '''
    获取tushare数据
    name：能够生成table名字，以‘sync_data_'+name命名
          同时也是tushare的api
          和Recoder中的name
    table_name: 用于在name相同的情况下区分数据库
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
    try:
        if not isCreate:
            # 计算更新参数，其中start_time是指向当前时间
            record = SyncRecoder.objects.get(name=name)
            start_time = datetime.datetime.now()
            factor = record.get('update').get('factor')
            if factor:
                end_time = handleTushareDate(start_time, factor)
            else:
                end_time = record.get('update_time')+ datetime.timedelta(days=1)
            if re.match(r'-',factor):
            # +1天是因为同步数据是包括头和尾的数据
                end_time = end_time + datetime.timedelta(days=1)
            kwargs['start_date'] = start_time.strftime('%Y%m%d')
            kwargs['end_date']= end_time.strftime('%Y%m%d')
            if kwargs.get('trade_date'):
                # 如果是同一天，则使用‘trade_date’参数
                kwargs['trade_date']= start_time.strftime('%Y%m%d')
                del kwargs['start_date']
                del kwargs['end_date']

        if name== 'pro_bar':
            data =ts.pro_bar(**kwargs)
        else :
            data = pro.query(name, **kwargs)

        data.to_sql(
            'sync_data_' + table_name if table_name else name,
            connect,
            if_exists='replace' if isCreate else 'append',
            index=False)
        status = 'success'
        # 初次获取数据后就将该任务加为周期任务
        if not isCreate:
            SyncRecoder.objects.update_or_create(
                name=name, defaults={
                    'status': status,
                })
        else:
            SyncRecoder.objects.update_or_create(
                name=name,
                defaults={
                    'status': status,
                    'period': period,
                    'start_time': kwargs.get('start_date'),
                    'end_time': kwargs.get('end_date'),
                    'task': self.name,
                    'params': json.dumps(kwargs),  # 先将dict转化为json字符串存入mysql
                    'describe': describe
                })
            if period:
                schedule, _ = CrontabSchedule.objects.get_or_create(**period)
                PeriodicTask.objects.get_or_create(
                    name=f'sync_{name}',
                    crontab=schedule,
                    task=self.name,
                    kwargs=json.dumps(kwargs.update(update)),
                    args=json.dumps(
                        [name, json.dumps(period), describe, False]))
    except Exception as e:
        status = 'failure'
        SyncRecoder.objects.update_or_create(
            name=name, defaults={
                'status': status,
            })
    finally:
        return {
            'detail': {
                'status': 'success',
                'task': self.name,
                'time': datetime.datetime.now()
            }
        }


def init_sync():
    tushare_to_sql.delay(
        name='stock_basic',
        describe='股票列表',
        isCreate=True,
        **{
            'exchange': '',
            'list_status': 'L',
            'fields': 'ts_code,symbol,name,area,industry,list_date'
        })

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
        table_name='stock',
        describe='',
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


def handleTushareDate(start_time, factor):
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


from cgi import parse
