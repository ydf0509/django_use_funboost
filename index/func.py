
from funboost import boost, BrokerEnum, ConcurrentModeEnum

@boost("test_django_queue",
       broker_kind=BrokerEnum.REDIS)
def create_report(x):
    print(f'x: {x}')
    return f"成功 {x}"