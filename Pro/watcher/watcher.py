from flask import Flask, render_template, url_for, Response
import sqlite3
import os
from flask import *
from scanner import Scanner

app = Flask(__name__)
app.secret_key=os.urandom(24)

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


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/signUp')
def about():
    return render_template('signUp.html')

   
@app.route('/adduser',methods = ["POST","GET"])
def adduser():  
  
    if request.method == "POST":  
        try:  
            username = request.form["username"]  
            email = request.form["email"]  
            password = request.form["password"]   
            with sqlite3.connect("admin.db") as con:  
                cur = con.cursor()  
                cur.execute("INSERT into Admin (username, email, password) values (?,?,?)",(username, email, password))  
                con.commit()               
        except:  
            con.rollback()  
        finally:  
            return redirect('/login')
            con.close()

@app.route('/response')
def response():  
    if 'ID' in session:
        return render_template('response.html') 
    else:    
        return redirect('/login') 


@app.route("/viewUser")  
def viewUser():  
    con = sqlite3.connect("admin.db")  
    con.row_factory = sqlite3.Row  
    cur = con.cursor()  
    cur.execute("select * from Admin")  
    rows = cur.fetchall()
    return render_template("viewUser.html",rows=rows)
            

@app.route('/loginValidation',methods = ["POST","GET"])
def loginValidation():  
    if request.method == "POST":  
          
            username = request.form["username"]  
            password = request.form["password"]   
            con = sqlite3.connect("admin.db")  
            con.row_factory = sqlite3.Row  
            cur = con.cursor()  
            cur.execute("select * from Admin WHERE username = ?",[username,])  
            cur.execute("select * from Admin WHERE password = ?",[password,])  
            rows = cur.fetchall()
             
            for row in rows :
                print (row) 
                if (username == row["username"]) and (password == row["password"]):                      
                        session['ID'] = rows[0][0]
                        return redirect('/response')  
                else :
                        return redirect('/login')  
  
            
@app.route('/logout')
def logout():  
    session.pop('ID')
    return redirect('/login') 

if __name__ == '__main__':
    app.run(debug=True)
