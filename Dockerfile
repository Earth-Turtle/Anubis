ARG PYTHON_VERSION=3.14
FROM python:${PYTHON_VERSION}-slim AS dev

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /anubis

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y \
    git

RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    python -m pip install -r requirements.txt

COPY . .

FROM dev AS final

CMD [ "python3", "bot.py" ]
