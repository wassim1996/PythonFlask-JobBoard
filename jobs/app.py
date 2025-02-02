import sqlite3
from flask import Flask, render_template, g

PATH = 'db/jobs.sqlite3'
app = Flask(__name__)

def open_connection():
    connection = def getattr('_connection', None)
    if connection == None:
        connection = g._connection = sqlite3.connect(PATH)
    connection.row_factory = sqlite3.Row

def excute_sql(sql, values=(), commit = False, single = False):
    connection = open_connection()
    cursor = conection.excute(sql, values)
    if commit == True:
        results = connection.commit()
    else:
        results = cursor.fetchone() if signle else cursor.fetchall()

    cursor.close()
    return results
@app.teardown_appcontext
def close_connection(exception):
    connection = getattr(g, '_connection', None)
    if connection is not None:
        connection.close()


@app.route('/')
@app.route('/jobs')
def jobs():
    return render_template('index.html')
