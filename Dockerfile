FROM python:3.9-alpine

RUN apk add postgresql-dev gcc python3-dev musl-dev

EXPOSE 8000

WORKDIR /app

COPY ./README.md ./version ./get_version.py ./setup.py ./

RUN pip install -e .
RUN pip install waitress

RUN rm ./README.md ./version ./get_version.py ./setup.py

COPY ./src/main/python .

CMD ["waitress-serve", "--port", "8000", "--url-scheme=http", "main:app"]