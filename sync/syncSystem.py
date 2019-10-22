'''
同步系统的运作流程，
1. 将dataFrame的数据格式的数据存储到数据库中，
2. 首次同步数据，并记录到同步表中，（后续可以通过同步表进行数据的自动同步）
3. 根据设置的时间自动设置周期，自动设置celery执行任务，
4. 任务每次执行都会根据同步数据表去拉取数据
'''

class SyncSystem(object):
    def __init__(self):
        pass

    def dataframe_to_sql(self, table_name, ):
        pass