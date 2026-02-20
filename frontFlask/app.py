from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(port=8000, debug=True)
    
    #FRONTEND
    # LEVANTAR SERVIDOR flask
    # C:\TAI204\frontFlask>python app.py
    #http://127.0.0.1:8000/