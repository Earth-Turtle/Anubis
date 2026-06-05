ARG PYTHON_VERSION=3.12
FROM python:${PYTHON_VERSION}-slim AS dev

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /anubis

RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    python -m pip install -r requirements.txt

COPY . .

FROM dev AS final

CMD [ "python3", "bot.py" ]
