from flask import Flask
from prometheus_client import make_wsgi_app
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from flask_prometheus_metrics import register_metrics
import psycopg2

app = Flask(__name__)

register_metrics(app, app_version="v0.1.2", app_config="staging")

app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/metrics': make_wsgi_app()
})

@app.route("/criar")
def indexBanco():
    con = psycopg2.connect(
        host='postgres',
        database='postgres',
        user='postgres',
        password='admin'
    )
    cur = con.cursor()
    sql = 'create table PUBLIC.cidade (id serial primary key, nome varchar(100), uf varchar(2))'
    cur.execute(sql)
    con.commit()
    return "criado"

@app.route("/")
def index():
    con = psycopg2.connect(
        host='postgres',
        database='postgres',
        user='postgres',
        password='admin'
    )
    cur = con.cursor()
    sql = "insert into PUBLIC.cidade values (default,'São Paulo','SP')"
    cur.execute(sql)
    con.commit()
    cur.execute('select * from cidade')
    recset = cur.fetchall()
    saida = ""
    for rec in recset:
        saida = f"{saida} {rec}"
    con.close()
    return saida

