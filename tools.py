from datetime import timedelta, time, datetime
from functools import wraps
from typing import Callable

last_invoke: dict[str, time] = {}

def cooldown[**P, R](name:str | None = None, cooldown: timedelta = timedelta(minutes=1)) -> Callable[P, R]:
    def wrap(f: Callable[P, R]) -> Callable[P, R]:
        nonlocal name
        if name is None: 
            name = f.__name__
        @wraps(f)
        def inner(*args: P.args, **kwargs: P.kwargs):
            cur_time = datetime.now
            if last_invoke[name] is None or last_invoke[name] + cooldown < cur_time:
                last_invoke[name] = cur_time
                return f(*args, **kwargs)
        return inner
    return wrap

def timer(name: str, cooldown: timedelta = timedelta(minutes=1)) -> bool:
    cur_time = datetime.now
    if last_invoke[name] is None or last_invoke[name] + cooldown < cur_time:
        last_invoke[name] = cur_time
        return True
    return False