from flask import Flask, render_template

app=Flask(__name__)
@app.route("/")
def webpage():
    return render_template("index.html",Myname="Aayesha Shaikh")
app.run()