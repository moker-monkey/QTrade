from __future__ import absolute_import, unicode_literals

from sqlalchemy import create_engine
import tushare as ts
# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from config import tushare as CT

from .celery import app as celery_app

ts.set_token(CT.TOKEN)
pro = ts.pro_api()
connect = create_engine(
    f'mysql+pymysql://{CT.DATABASE_USERNAME}:{CT.DATABASE_PASSWORD}@localhost:3306/{CT.DATABASE_NAME}?charset=utf8'
)

__all__ = ('celery_app', 'pro', 'connect')  #设置导出的范围
