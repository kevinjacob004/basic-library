from flask import Flask, render_template,request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

cl=MongoClient()
db=cl["library"]
col=db["library"]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/add",methods=["POST"])
def add_book():
    bookname=request.form["bookname"]
    count=int(request.form["count"])
    author=request.form["author"]

    data={"bookname":bookname,"count":count,"author":author}

    col.insert_one(data)
    return "Book added successfully. <a href='/details'>View all books</a>"

@app.route("/details")
def showbooks():
    books=list(col.find())
    return render_template("details.html",books=books)

if __name__ == "__main__":
    print(123)
    app.run(host="0.0.0.0",debug=True,port = 8000)