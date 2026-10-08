from flask import Flask

app=Flask(__name__)
@app.route("/")
def home():
    return "Teri maa ki choot 4 baar bhosdike madarchod"

if __name__=="__main__":
    app.run(debug=True)