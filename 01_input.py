from flask import Flask
from flask import request
import logging 
logging.basicConfig(filename="01_logging.log", level=logging.DEBUG, format='%(asctime)s %(message)s')
app= Flask(__name__)

try: 
    logging.info("creating a test route")
    @app.route("/test")
    def test():
        logging.info("taking input")
        data = request.args.get('x')
        logging.info("returning the data input")
        return "Entered DATA :{}".format(data)
    
except Exception as e:
    logging.info("Error:{}".format(e))

else :
    logging.info("no error")

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5050)

