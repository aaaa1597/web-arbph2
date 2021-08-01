from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
  return render_template('index.html')

@app.route("/getTickerBi", methods=['post'])
def gettickerbi():
  print(request.json['pair'])
  return {'ask' : 500.1, 'bid' : 500.2}

@app.route("/getTickerFx", methods=['post'])
def getTickerfx():
  print(request.json['pair'])
  return {'ask' : 500.1, 'bid' : 500.3}

@app.route("/getTickerKc", methods=['post'])
def getTickerkc():
  print(request.json['pair'])
  return {'ask' : 500.1, 'bid' : 500.4}

@app.route("/getTickerBs", methods=['post'])
def getTickerbs():
  print(request.json['pair'])
  return {'ask' : 500.1, 'bid' : 500.5}

@app.route("/getTickerPn", methods=['post'])
def getTickerpn():
  print(request.json['pair'])
  return {'ask' : 500.1, 'bid' : 500.6}

@app.route("/getTickerBt", methods=['post'])
def getTickerbt():
  print(request.json['pair'])
  return {'ask' : 500.1, 'bid' : 500.7}

@app.route("/getTickerEx", methods=['post'])
def getTickerex():
  print(request.json['pair'])
  return {'ask' : 500.1, 'bid' : 500.8}

@app.route("/getTickerLq", methods=['post'])
def getTickerlq():
  print(request.json['pair'])
  return {'ask' : 500.1, 'bid' : 500.9}

@app.route("/getTickerBb", methods=['post'])
def getTickerbb():
  print(request.json['pair'])
  return {'ask' : 500.1, 'bid' : 501.0}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
