from flask import Flask,request
import flask

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['POST','GET','OPTIONS'])
def home():
    data=request.get_data()
    return "hello from myhapp"

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=80)