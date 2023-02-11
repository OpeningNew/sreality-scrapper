import psycopg2
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    conn = psycopg2.connect(
        host="database",
        user="postgres",
        password="supersecretpassword",
        dbname="postgres",
    )
    cur = conn.cursor()
    cur.execute(
        "select exists(select from information_schema.tables where table_name=%s)",
        ("properties",),
    )
    properties = []
    if cur.fetchone()[0]:
        cur.execute("SELECT * FROM properties;")
        properties = cur.fetchall()
    cur.close()
    conn.close()

    return render_template("index.html", properties=properties)
