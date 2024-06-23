from flask import Flask
from flask import request
from flask import render_template,jsonify
import logging 
logging.basicConfig(filename="00_logging.log", level=logging.DEBUG, format='%(asctime)s %(message)s')
app= Flask(__name__)
try:
    @app.route('/',methods=['GET','POST'])
    def claculator():
        return render_template('00_index.html')
    
    @app.route("/calc",methods=['POST'])
    def calculate():
       if(request.method == 'POST'):
        ops = request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        if (ops == 'add'):
            r = num1+num2
            result = "The sum of " + str(num1) + ' and ' + str(num2) + " is " + str(r)
        if (ops == 'subtract'):
            r = num1-num2
            result = "The subtract of " + str(num1) + ' and ' + str(num2) + " is " + str(r)
        if (ops == 'multiply'):
            r = num1*num2
            result = "The multiply of " + str(num1) + ' and ' + str(num2) + " is " + str(r)
        if (ops == 'divide'):
            r = num1/num2
            result = "The divide of " + str(num1) + ' and ' + str(num2) + " is " + str(r)
            
        return render_template('01_results.html' , result = result)
       
    
    logging.info("creating basic routes and defining functions to show data")
    @app.route("/hello_world")
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
    app.run(host="0.0.0.0",port=5050)
