from flask import Flask, render_template, session, redirect # redirect to avoid date being handled more than once
# session stores valuable data for future use
app = Flask(__name__)

app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes

@app.route('/')
def index():
    if "count" not in session:
        session["count"] = 0
    if "count" in session: 
        session["count"] += 1 #add 1 to counter
    return render_template("index.html")

@app.route('/destroy') # for route '/destroy', parameter in the url will reset counter
def destroy():
    session.clear() #session will clear user's info when app is not being used
    return redirect('/') 

if __name__=="__main__":
    app.run(debug=True)