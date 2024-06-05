from flask import Flask,render_template
app=Flask(__name__)
@app.route("/sara")
def hello():
    return "<h1>Annamalai</h1>"
@app.route("/karthi")
def hai():
    return "Karthi"

if __name__ =="__main__":
    app.run(debug=True,port=2004)