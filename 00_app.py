from flask import Flask
from flask import request
from flask import render_template,jsonify
import logging 
logging.basicConfig(filename="00_logging.log", level=logging.DEBUG, format='%(asctime)s %(message)s')
app= Flask(__name__)
try:
    @app.route("/calculator",methods=['GET','POST'])
    def claculator():
        return render_template('index.html')
    
    logging.info("creating basic routes and defining functions to show data")
    @app.route("/")
    def hello_world():
        return "<h1>HELLO WORLD!</h1>"

    @app.route("/hello_world1")
    def hello_world1():
        return "<h1> HELLO WORLD2!"

except Exception as e :
    logging.info("Error:{}".format(e))

else :
    logging.info("NO ERROR")

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)
