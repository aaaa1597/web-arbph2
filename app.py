from flask import Flask, render_template, request
app = Flask(__name__)

import GetTicker

@app.route("/")
def index():
  return render_template('index.html')

@app.route("/getTickerBi", methods=['post'])
def getTickerbi():
  pair = request.json['pair'].replace('(T)', 'T').replace('/', '')
  ret = GetTicker.getTickerBi(pair)['bi']
  return {'bid':ret['tksbid'], 'ask':ret['tksask']}

@app.route("/getTickerFx", methods=['post'])
def getTickerfx():
  return GetTicker.getTickerFx(request.json['pair'])

@app.route("/getTickerKc", methods=['post'])
def getTickerkc():
  return GetTicker.getTickerKc(request.json['pair'])

@app.route("/getTickerBs", methods=['post'])
def getTickerbs():
  return GetTicker.getTickerBs(request.json['pair'])

@app.route("/getTickerPn", methods=['post'])
def getTickerpn():
  return GetTicker.getTickerPn(request.json['pair'])

@app.route("/getTickerBt", methods=['post'])
def getTickerbt():
  return GetTicker.getTickerBt(request.json['pair'])

@app.route("/getTickerEx", methods=['post'])
def getTickerex():
  return GetTicker.getTickerEx(request.json['pair'])

@app.route("/getTickerLq", methods=['post'])
def getTickerlq():
  return GetTicker.getTickerLq(request.json['pair'])

@app.route("/getTickerBb", methods=['post'])
def getTickerbb():
  return GetTicker.getTickerBb(request.json['pair'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
