import jaydebeapi
import os
import src.queries as queries
from flask import Flask, render_template

app = Flask(__name__)

# os.environ["JAVA_HOME"] = "C:\\Program Files\\Java\\jdk-21"


def make_connection(query):
    def connect(db_driver_path: str, db_url: str, db_user: str, db_password: str) -> jaydebeapi.Connection:
        conn = jaydebeapi.connect("org.h2.Driver", db_url, [db_user, db_password], db_driver_path)
        return conn

    path_to_h2_jar: str = open("src/path_to_h2_jar", "r").read()
    url: str = "jdbc:h2:~/test"
    user: str = "sa"
    password: str = ""
    connection: jaydebeapi.Connection = connect(path_to_h2_jar, url, user, password)
    curs: jaydebeapi.Cursor = connection.cursor()
    curs.execute(query)
    data = curs.fetchall()
    curs.close()
    connection.close()
    return data


@app.route("/index.html", methods=['GET', 'POST'])
def index():
    data1 = make_connection(queries.query1())
    data2 = make_connection(queries.query2())

    return render_template("index.html", data1=data1, data2=data2)


@app.route("/populations/<year>/<period>/<name>.html", methods=['GET', 'POST'])
def population(year, period, name):
    data3 = make_connection(queries.query3(name, year, period))
    data4 = make_connection(queries.query4(name, year, period))
    return render_template("pop.html", year=year, period=period, name=name, data3=data3, data4=data4)


@app.route("/grades/<year>/<period>/<name>.html", methods=['GET', 'POST'])
def grade(year, period, name):
    data = make_connection(queries.query5(name, year, period))
    return render_template("grades.html", year=year, period=period, name=name, data=data)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
