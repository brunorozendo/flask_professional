FROM python:3.9-alpine

RUN apk add postgresql-dev gcc python3-dev musl-dev

EXPOSE 8000

WORKDIR /app

ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8000


COPY ./README.md ./version ./get_version.py ./setup.py ./
# RUN pip install -e .[dev,unit,integration]

RUN pip install -e .

COPY ./src/main/python .

CMD ["flask", "run"]
