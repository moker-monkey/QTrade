'''
setting of celery
1. start celery-beat:celery -A QTrade beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
2. start celery worker: celery worker -A QTrade -l info
3. start celery flower: python manage.py celery flower    #defalut url is http://localhost:5555
start RabbitMQ：sudo rabbitmq-server
background start: -detached
check status: sudo rabbitmqctl status
close RabbitMQ: sudo rabbitmq-server -stop
'''

BROKER_URL = 'amqp://xiaochangming:xcm532621@localhost:5672//'

TASK_SERIALIZER = 'json'
RESULT_SERIALIZER = 'json'
ACCEPT_CONTENT = ['json']
TIMEZONE = 'Asia/Shanghai'
ENABLE_UTC = True

CELERY_RESULT_BACKEND = 'django-db'
CELERY_CACHE_BACKEND = 'django-cache'
