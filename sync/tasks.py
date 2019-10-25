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

def mergeUpdateToParams(params,update){
    '''
    用于处理更新的params
    '''
    record = SyncRecoder.objects.get(name=inner_name)
    start_time = datetime.datetime.now()
    factor = record.get('update').get('factor')
    if factor:
        end_time = handleTushareDate(start_time, factor)
    else:
        end_time = record.get('update_time') + datetime.timedelta(
            days=1)
    if re.match(r'-', factor):
        # +1天是因为同步数据是包括头和尾的数据
        end_time = end_time + datetime.timedelta(days=1)
    params['start_date'] = start_time.strftime('%Y%m%d')
    params['end_date'] = end_time.strftime('%Y%m%d')
    if params.get('trade_date'):
        # 如果是同一天，则使用‘trade_date’参数
        params['trade_date'] = start_time.strftime('%Y%m%d')
        del params['start_date']
        del params['end_date']
    return params
}

def get_tushare(name, isCreate, params, alias=''):
    try:
        if name == 'shibor':
            data = pro.shibor(**params)
        elif alias:
            data = ts.pro_bar(**params)
        else:
            data = pro.query(name, **params)
        return {'status':'success',:data:'data'}
    except expression as e:
        return {
            'status':'failure',
            'error':e
        }



def set_database(name,data,isCreate, connect, alias=''):
    try:
        data.to_sql(
            'sync_data_' + alias if alias else 'sync_data_' + name,
            connect,
            if_exists='replace' if isCreate else 'append',
            index=False)
        return {
            'status':'success'
        }
    except expression as e
        return {
            'status':'failurl',
            'error':e
        }

def set_recoder(name,task,status,period,params,update,describe,alias='',e=''):
    try:
        SyncRecoder.objects.update_or_create(
            name=name,
            defaults={
                'status': status,
                'period': period,
                'task': self.name,
                'params': json.dumps(params),  # 先将dict转化为json字符串存入mysql
                'update': update,
                'describe': describe,
                'alias': alias,
                'error':e
            })
        return {
            'status':'success'
        }
    except expression as e:
        return {
            'status':'failurl',
            'error':e
        }


def set_periodic_task(name,period,task,alias='',params={},update={}):
    try:
        schedule, _ = CrontabSchedule.objects.get_or_create(**period)
        PeriodicTask.objects.update_or_create(
            name=f'sync_{inner_name}',
            defaults={
                'crontab':
                schedule,
                'task':
                self.name,
                'kwargs':
                json.dumps(params.update(update)),
                'args':
                json.dumps([
                    name,
                    json.dumps(period), describe, False, alias
                ])
            })
    except expression as e:
        return {
            'status':'failurl',
            'error':e
        }
    

@shared_task(bind=True)
def tushare_to_sql(self,name,describe,isCreate,alias='',period={},params={},update={}):
    status=''
    inner_name=alias if alias else name
    if not isCreate:

