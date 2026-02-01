from datetime import timedelta, datetime
from functools import wraps
import logging
from typing import Awaitable, Callable, Union

last_invoke: dict[str, datetime] = {}

def cooldown[**P, R](name:str | None = None, cooldown: timedelta = timedelta(minutes=1)):
    def wrap(f: Callable[P, R]) -> Callable[P, Union[None, R]]:
        @wraps(f)
        def inner(*args: P.args, **kwargs: P.kwargs):
            if timer(name if name else f.__name__, cooldown):
                return f(*args, **kwargs)
        return inner
    return wrap

def cooldown_async[**P, R](name: str | None = None, cooldown: timedelta = timedelta(minutes=1)):
    async def wrap(f: Callable[P, Awaitable[R]]) -> Callable[P, Awaitable[Union[None, R]]]:
        @wraps(f)
        async def inner(*args: P.args, **kwargs: P.kwargs):
            if timer(name if name else f.__name__, cooldown):
                return await f(*args, **kwargs)
        return inner
    return wrap

def timer(name: str, cooldown: timedelta = timedelta(minutes=1)) -> bool:
    cur_time = datetime.now()
    last_time_invoked = last_invoke.get(name)
    if last_time_invoked is None or last_time_invoked + cooldown < cur_time:
        last_invoke[name] = cur_time
        return True
    logging.debug("Timer failed for " + name)
    return False