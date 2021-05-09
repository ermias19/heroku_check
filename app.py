from flask import Flask, session, render_template ,redirect ,request,url_for, flash, session 

app = Flask(__name__)


@app.route("/")

def home():
   return "hi"

if __name__ == '__main__':
    app.run( port="8000")