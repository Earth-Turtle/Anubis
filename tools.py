from datetime import timedelta, time, datetime

last_invoke: dict[str, time] = {}

def cooldown(name: str = None, cooldown: timedelta = timedelta(minutes=1)) -> function:
    def wrap(f: function) -> function:
        nonlocal name
        if name is None: name = f.__name__
        def inner(*args, **kwargs):
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