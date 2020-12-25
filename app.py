from flask import Flask, flash, redirect, render_template, request, session, abort
app = Flask(__name__)

@app.route("/")
def index():
    return "Index!"



@app.route("/navidad/<string:name>/<string:name_1>")
def hello(name,name_1):
    return render_template(
        'test.html',name=name,name_1=name_1)


if __name__ == "__main__":
    app.run("0.0.0.0",debug=False)
    #app.run("0.0.0.0",debug=True)
