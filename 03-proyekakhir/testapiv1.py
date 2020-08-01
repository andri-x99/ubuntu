import sqlite3, time, threading
from flask import jsonify, request, Flask, json
from dictor import dictor

app = Flask('hehe')

# Melakukan koneksi ke database
def database():
    con = sqlite3.connect('logsql-internet.sqlite')
    return con

# Cursor
def getData(result, cur):
    data= []
    for i in range(len(result)):
        x = dict(
                zip([c[0] for c in cur.description], 
                result[i])
            )
        data.append(x)
    return data

# Memanggil semua data yang terdapat pada tabel Connections
@app.route('/connections')
def get1():
    d = database()
    c = d.cursor()
    result = c.execute("select * from connections").fetchall()
    data = getData(result, c)
    return jsonify(data)
# Menghapus semua data yang terdapat pada tabel Connections
@app.route('/connections/delete')
def delete1():
    d = database()
    c = d.cursor()
    result = c.execute("delete from connections").fetchall()
    d.commit()
    data = getData(result, c)
    return jsonify(data)

@app.route('/logins')
def get2():
    d = database()
    c = d.cursor()
    result = c.execute("select * from logins").fetchall()
    data = getData(result, c)
    return jsonify(data)
@app.route('/logins/delete')
def delete2():
    d = database()
    c = d.cursor()
    result = c.execute("delete from logins").fetchall()
    d.commit()
    data = getData(result, c)
    return jsonify(data)

@app.route('/dcerpcrequests')
def get3():
    d = database()
    c = d.cursor()
    result = c.execute("select * from dcerpcrequests").fetchall()
    data = getData(result, c)
    return jsonify(data)
@app.route('/dcerpcrequests/delete')
def delete3():
    d = database()
    c = d.cursor()
    result = c.execute("delete from dcerpcrequests").fetchall()
    d.commit()
    data = getData(result, c)
    return jsonify(data)

@app.route('/dcerpcbinds')
def get4():
    d = database()
    c = d.cursor()
    result = c.execute("select * from dcerpcbinds").fetchall()
    data = getData(result, c)
    return jsonify(data)
@app.route('/dcerpcbinds/delete')
def delete4():
    d = database()
    c = d.cursor()
    result = c.execute("delete from dcerpcbinds").fetchall()
    d.commit()
    data = getData(result, c)
    return jsonify(data)

@app.route('/offers')
def get5():
    d = database()
    c = d.cursor()
    result = c.execute("select * from offers").fetchall()
    data = getData(result, c)
    return jsonify(data)
@app.route('/offers/delete')
def delete5():
    d = database()
    c = d.cursor()
    result = c.execute("delete from offers").fetchall()
    d.commit()
    data = getData(result, c)
    return jsonify(data)

@app.route('/downloads')
def get6():
    d = database()
    c = d.cursor()
    result = c.execute("select * from downloads").fetchall()
    data = getData(result, c)
    return jsonify(data)
@app.route('/downloads/delete')
def delete6():
    d = database()
    c = d.cursor()
    result = c.execute("delete from downloads").fetchall()
    d.commit()
    data = getData(result, c)
    return jsonify(data)

@app.route('/mssql_commands')
def get7():
    d = database()
    c = d.cursor()
    result = c.execute("select * from mssql_commands").fetchall()
    data = getData(result, c)
    return jsonify(data)
@app.route('/mssql_commands/delete')
def delete7():
    d = database()
    c = d.cursor()
    result = c.execute("delete from mssql_commands").fetchall()
    d.commit()
    data = getData(result, c)
    return jsonify(data)

@app.route('/mssql_fingerprints')
def get8():
    d = database()
    c = d.cursor()
    result = c.execute("select * from mssql_fingerprints").fetchall()
    data = getData(result, c)
    return jsonify(data)
@app.route('/mssql_fingerprints/delete')
def delete8():
    d = database()
    c = d.cursor()
    result = c.execute("delete from mssql_fingerprints").fetchall()
    d.commit()
    data = getData(result, c)
    return jsonify(data)

@app.route('/mysql_commands')
def get9():
    d = database()
    c = d.cursor()
    result = c.execute("select * from mysql_commands").fetchall()
    data = getData(result, c)
    return jsonify(data)
@app.route('/mysql_commands/delete')
def delete9():
    d = database()
    c = d.cursor()
    result = c.execute("delete from mysql_commands").fetchall()
    d.commit()
    data = getData(result, c)
    return jsonify(data)

@app.route('/mysql_command_args')
def get10():
    d = database()
    c = d.cursor()
    result = c.execute("select * from mysql_command_args").fetchall()
    data = getData(result, c)
    return jsonify(data)
@app.route('/mysql_command_args/delete')
def delete10():
    d = database()
    c = d.cursor()
    result = c.execute("delete from mysql_command_args").fetchall()
    d.commit()
    data = getData(result, c)
    return jsonify(data)

@app.route('/mysql_command_ops')
def get11():
    d = database()
    c = d.cursor()
    result = c.execute("select * from mysql_command_ops").fetchall()
    data = getData(result, c)
    return jsonify(data)
@app.route('/mysql_command_ops/delete')
def delete11():
    d = database()
    c = d.cursor()
    result = c.execute("delete from mysql_command_ops").fetchall()
    d.commit()
    data = getData(result, c)
    return jsonify(data)

# Setting Flask dalam mode debug, agar ketika ada perubahan yang terjadi, akan langsung memuat ulang halaman
app.run(debug=True, host='10.33.109.242')
