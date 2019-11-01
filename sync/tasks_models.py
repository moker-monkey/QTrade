from celery import Task

class LoopTask(Task):
    _list = None

    def getList(self, model):
        '''
        传入model已获取列表
        '''
        _list = model.objects.all()
        return _list
    