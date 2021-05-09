from flask import Flask, session, render_template ,redirect ,request,url_for, flash, session 

app = Flask(__name__)
app.config['SECRET_KEY']='5791628bb0b13ce0c676dfde280ba245'

@app.route("/", methods=['GET', 'POST'])

def home():
   return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True, port="8000")