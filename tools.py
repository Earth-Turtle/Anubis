from datetime import timedelta, datetime
from functools import wraps
from typing import Callable, Union

last_invoke: dict[str, datetime] = {}

def cooldown[**P, R](name:str | None = None, cooldown: timedelta = timedelta(minutes=1)) -> Callable[[Callable[P, R]], Callable[P, Union[None, R]]]:
    def wrap(f: Callable[P, R]) -> Callable[P, Union[None, R]]:
        nonlocal name
        cooldown_name = name if name else f.__name__
        @wraps(f)
        def inner(*args: P.args, **kwargs: P.kwargs):
            if timer(cooldown_name, cooldown):
                return f(*args, **kwargs)
        return inner
    return wrap

def timer(name: str, cooldown: timedelta = timedelta(minutes=1)) -> bool:
    cur_time = datetime.now()
    last_time_invoked = last_invoke.get(name)
    if last_time_invoked is None or last_time_invoked + cooldown < cur_time:
        last_invoke[name] = cur_time
        return True
    return False