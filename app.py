from flask import Flask,request,jsonify, render_template,send_from_directory
import os
from flask_cors import CORS,cross_origin
from main import main
app = Flask(__name__,static_folder='build')



script_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_directory)

CORS(app) 





@app.route("/api",methods=['GET','POST'])
def hello_world():
    if request.method=='POST':
      content=request.get_json()
      response = main(content['details'])
      response=response.tolist()
      return jsonify(response)
    else:
       return "404 not found"

if __name__=="__main__":
    app.run(debug=True)