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
from .tasks_models import LoopTask
from sync_db.models import SyncDataStockBasic


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


def changeParams(name, params, update, alias=''):
    '''
    用于更新tushare的参数的函数
    暂时使用手动同步
    '''
    # inner_name = alias if alias else name
    # record = SyncRecoder.objects.get(name=inner_name)
    # start_time = datetime.datetime.now()
    # if params.get('start_date'):
    #     factor = update.get('factor')
    #     if factor:
    #         end_time = handleFactorDate(start_time, factor)
    #         if re.match(r'-', factor):
    #             end_time = end_time + datetime.timedelta(days=1)
    #     else:
    #         end_time = record.update_time + datetime.timedelta(days=1)

    #     params['start_date'] = start_time.strftime('%Y%m%d')
    #     params['end_date'] = end_time.strftime('%Y%m%d')
    #     if params.get('trade_date'):
    #         params['trade_date'] = start_time.strftime('%Y%m%d')
    #         del params['start_date']
    #         del params['end_date']
    return params


def get_tushare(name, params, alias=''):
    '''
    用于获取tushare数据的回调函数
    '''
    try:
        if name == 'shibor':
            data = pro.shibor(**params)
        elif name == 'stock_company':
            data = pro.stock_company(**params)
        elif name == 'express':
            data = pro.express(**params)
        elif name == 'disclosure_date':
            data = pro.disclosure_date(**params)
        elif name == 'pro_bar':
            data = ts.pro_bar(**params)
        else:
            data = pro.query(name, **params)
        return data
    except Exception as e:
        raise Exception(f'获取数据失败:{e}')


def data_to_sql_create(data, name, isCreate, connect, alias=''):
    try:
        data.to_sql(
            'sync_data_' + alias if alias else 'sync_data_' + name,
            connect,
            if_exists='replace' if isCreate else 'append',
            index=False)
        return {'status': 'success'}
    except Exception as e:
        raise Exception(f'存储数据失败：{e}')


def update_or_create_recoder(name, defaults, alias=''):
    pass
    # 用于记录更新时间
    # inner_name = alias if alias else name
    # try:
    #     SyncRecoder.objects.update_or_create(
    #         name=inner_name, defaults=defaults)
    # except Exception as e:
    #     raise Exception(f'更新或者创建记录失败：{e}')


def createPeriodicTask(name,
                       describe,
                       period,
                       task,
                       alias='',
                       field='',
                       wait=0,
                       params={},
                       update={}):
    inner_name = alias if alias else name
    try:
        schedule, _ = CrontabSchedule.objects.get_or_create(**period)
        if field:
            # 创建周期循环获取数据
            PeriodicTask.objects.update_or_create(
                name=f'sync_{inner_name}',
                defaults={
                    'crontab':
                    schedule,
                    'task':
                    task,
                    'args':
                    json.dumps([
                        name, describe, False, alias, period, params, update,
                        field, wait
                    ])
                })
        else:
            # 创建周期获取数据
            PeriodicTask.objects.update_or_create(
                name=f'sync_{inner_name}',
                defaults={
                    'crontab':
                    schedule,
                    'task':
                    task,
                    'args':
                    json.dumps(
                        [name, describe, False, alias, period, params, update])
                })
    except Exception as e:
        raise Exception(f'周期任务创建失败，{e}')


@shared_task(bind=True)
def auto_to_sql(self,
                name,
                describe,
                isCreate,
                alias='',
                period={},
                params={},
                update={}):
    # 存储都使用json的字符串格式，调用都需要把json转为json dict
    status = ''
    params_temp = {}
    inner_name = alias if alias else name
    if not isCreate and period:
        # 如果是更新就通过传入的方法计算参数
        params_temp = changeParams(
            name=name, alias=alias, params=params, update=update)
    inner_params = params if isCreate or not period else params_temp
    try:
        data = get_tushare(
            name=name,
            params=inner_params,
            alias=alias,
        )  # 获取data
        data_to_sql_create(
            name=name,
            data=data,
            isCreate=isCreate,
            connect=connect,
            alias=alias)
        if isCreate:
            update_or_create_recoder(
                name=name,
                defaults={
                    'status': 'success',
                    'period': period,
                    'task': self.name,
                    'params': inner_params,  # 先将dict转化为json字符串存入mysql
                    'update': update,
                    'describe': describe,
                    'alias': alias,
                })  # 创建记录
            if period:
                createPeriodicTask(
                    name=name,
                    period=period,
                    describe=describe,
                    task=self.name,
                    alias=alias,
                    params=inner_params,
                    update=update)  # 创建周期任务
        else:
            update_or_create_recoder(
                name=inner_name,
                alias=alias,
                defaults={
                    'status': 'success',
                    'error': ''
                })  # 更新记录

    except Exception as e:
        update_or_create_recoder(
            name=inner_name,
            defaults={
                'alias': alias,
                'status': 'failurl',
                'error': e
            })
    finally:
        return {
            'detail': {
                'name': inner_name,
                'status': 'success',
                'task': self.name,
                'time': datetime.datetime.now()
            }
        }


@shared_task(bind=True, base=LoopTask)
def loopstock_to_sql(
        self,
        name,
        describe,
        isCreate,
        alias='',
        period={},
        params={},
        update={},
        field='',
        wait=5,
):
    '''
    该任务为循环同步数据所使用，因为记录也不同，因此需要重新记录
    '''
    stock_list = loopstock_to_sql.getList(SyncDataStockBasic)
    if not isCreate and period:
    # 如果是更新就通过传入的方法计算参数
        params_temp = changeParams(name=name, alias=alias, params=params, update=update)
    inner_params = params if isCreate or not period else params_temp
    for idx, val in enumerate(stock_list):
        field_val = eval(f'val.{field}')
        params.update({'ts_code': field_val})
        data = get_tushare(
            name=name,
            params=params,
            alias=alias,
        )  # 获取data
        print(f'{idx+1}/{len(stock_list)}')
        if not idx and isCreate:
            inner_isCreate = True
        else:
            inner_isCreate = False
        data_to_sql_create(
            name=name,
            data=data,
            isCreate=inner_isCreate,
            connect=connect,
            alias=alias)
        time.sleep(wait)

    if isCreate:
        update_or_create_recoder(
            name=name,
            defaults={
                'status': 'success',
                'period': period,
                'task': self.name,
                'params': params,
                'update': update,
                'describe': describe,
                'alias': alias,
                'field': field,
                'wait': wait
            })  # 创建记录
        if period:
            createPeriodicTask(
                name=name,
                period=period,
                describe=describe,
                task=self.name,
                alias=alias,
                field=field,
                wait=wait,
                params=params,
                update=update)  # 创建周期任务
    else:
        update_or_create_recoder(
            name=name,
            alias=alias,
            defaults={
                'status': 'success',
                'error': ''
            })  # 更新记录
