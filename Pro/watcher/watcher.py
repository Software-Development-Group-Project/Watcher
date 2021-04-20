from flask import Flask, render_template, url_for, Response
import sqlite3
from flask import *
from scanner import Scanner

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/help')
def help():
    return render_template('help.html')


@app.route('/live')
def live():
    return render_template('live.html')


@app.route("/member")
def index():
    return render_template("index.html");


@app.route("/add")
def add():
    return render_template("add.html")


@app.route("/savedetails", methods=["POST", "GET"])
def saveDetails():
    msg = "msg"
    if request.method == "POST":
        try:
            name = request.form["name"]
            email = request.form["email"]
            address = request.form["address"]
            number = request.form["number"]
            with sqlite3.connect("members.db") as con:
                cur = con.cursor()
                cur.execute("INSERT into Members (name, email, address, number) values (?,?,?,?)",
                            (name, email, address, number))
                con.commit()
                msg = "Member successfully Added"
        except:
            con.rollback()
            msg = "We can not add the employee to the list"
        finally:
            con.close()
            return render_template("success.html", msg=msg)


@app.route("/view")
def view():
    con = sqlite3.connect("members.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from Members")
    rows = cur.fetchall()
    return render_template("view.html", rows=rows)


@app.route("/delete")
def delete():
    return render_template("delete.html")


@app.route("/deleterecord", methods=["POST"])
def deleterecord():
    id = request.form["id"]
    with sqlite3.connect("members.db") as con:
        try:
            cur = con.cursor()
            cur.execute("delete from Members where id = ?", id)
            msg = "record successfully deleted"
        except:
            msg = "can't be deleted"
        finally:
            return render_template("delete_record.html", msg=msg)


def gen(scanner):
    while True:
        frame = scanner.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(gen(Scanner()), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(debug=True)
