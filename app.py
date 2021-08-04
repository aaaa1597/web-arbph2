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
  pair = request.json['pair'].replace('(T)', 'T')
  ret = GetTicker.getTickerFx(pair)['fx']
  return {'bid':ret['tksbid'], 'ask':ret['tksask']}

@app.route("/getTickerKc", methods=['post'])
def getTickerkc():
  pair = request.json['pair'].replace('(T)', 'T').replace('/', '-')
  ret = GetTicker.getTickerKc(pair)['kc']
  return {'bid':ret['tksbid'], 'ask':ret['tksask']}

@app.route("/getTickerBs", methods=['post'])
def getTickerbs():
  pair = request.json['pair'].replace('(T)', 'T').replace('/', '').lower()
  ret = GetTicker.getTickerBs(pair)['bs']
  return {'bid':ret['tksbid'], 'ask':ret['tksask']}

@app.route("/getTickerPn", methods=['post'])
def getTickerpn():
  pairs = request.json['pair'].replace('(T)', 'T').split('/')
  pair = pairs[1] + '_' + pairs[0]
  ret = GetTicker.getTickerPn(pair)['pn']
  'USDT_BTC'
  return {'bid':ret['tksbid'], 'ask':ret['tksask']}

@app.route("/getTickerBt", methods=['post'])
def getTickerbt():
  pair = request.json['pair'].replace('(T)', 'T').replace('/', '-')
  ret = GetTicker.getTickerBt(pair)['bt']
  return {'bid':ret['tksbid'], 'ask':ret['tksask']}

@app.route("/getTickerEx", methods=['post'])
def getTickerex():
  pair = request.json['pair'].replace('(T)', 'T').replace('/', '-')
  ret = GetTicker.getTickerEx(pair)['ex']
  return {'bid':ret['tksbid'], 'ask':ret['tksask']}

@app.route("/getTickerLq", methods=['post'])
def getTickerlq():
  return GetTicker.getTickerLq(request.json['pair'])

@app.route("/getTickerBb", methods=['post'])
def getTickerbb():
  return GetTicker.getTickerBb(request.json['pair'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
