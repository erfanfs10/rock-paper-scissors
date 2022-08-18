from datetime import datetime

CHOICES = ['r', 'p', 's']


def cal_time(func):
    def wrap(*args, **kwargs):
        start = datetime.now()
        rv = func(*args, **kwargs)
        res = datetime.now() - start
        print(f"total time : {str(res)[:7]}")
        return rv
    return wrap

