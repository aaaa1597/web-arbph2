from flask import Flask, render_template, request
app = Flask(__name__)

import GetTicker

@app.route("/")
def index():
  return render_template('index.html')

@app.route("/getTickerBi", methods=['post'])
def getTickerbi():
  pair = request.json['pair'].replace('_', '')
  ret = GetTicker.getTickerBi(pair)['bi']
  retpair = ret['symbol'].replace('USDT', '_USDT')
  if 'errormsg' in ret:
    return {'bid':'---', 'ask':'---', 'broker':'bi', 'pair':retpair}
  else:
    return {'bid':float(ret['tksbid']), 'ask':float(ret['tksask']), 'broker':ret['tksbroker'], 'pair':retpair}

@app.route("/getTickerFx", methods=['post'])
def getTickerfx():
  pair = request.json['pair']
  ret = GetTicker.getTickerFx(pair)['fx']
  retpair = ret['symbol'].replace('/', '_')
  if 'errormsg' in ret:
    return {'bid':'---', 'ask':'---', 'broker':'fx', 'pair':retpair}
  else:
    return {'bid':float(ret['tksbid']), 'ask':float(ret['tksask']), 'broker':ret['tksbroker'], 'pair':retpair}

@app.route("/getTickerKc", methods=['post'])
def getTickerkc():
  pair = request.json['pair'].replace('_', '-')
  ret = GetTicker.getTickerKc(pair)['kc']
  retpair = ret['symbol'].replace('-', '_')
  if 'errormsg' in ret:
    return {'bid':'---', 'ask':'---', 'broker':'kc', 'pair':retpair}
  else:
    return {'bid':float(ret['tksbid']), 'ask':float(ret['tksask']), 'broker':ret['tksbroker'], 'pair':retpair}

@app.route("/getTickerBs", methods=['post'])
def getTickerbs():
  pair = request.json['pair'].replace('_', '').lower()
  ret = GetTicker.getTickerBs(pair)['bs']
  retpair = ret['symbol'].replace('usdt', '_USDT').upper()
  if 'errormsg' in ret:
    return {'bid':'---', 'ask':'---', 'broker':'bs', 'pair':retpair}
  else:
    return {'bid':float(ret['tksbid']), 'ask':float(ret['tksask']), 'broker':ret['tksbroker'], 'pair':retpair}

@app.route("/getTickerPn", methods=['post'])
def getTickerpn():
  pairs = request.json['pair'].split('_')
  pair = pairs[1] + '_' + pairs[0]
  ret = GetTicker.getTickerPn(pair)['pn']
  retpair = ret['symbol'].split('_')
  retpair = retpair[1] + '_' + retpair[0]
  if 'errormsg' in ret:
    return {'bid':'---', 'ask':'---', 'broker':'pn', 'pair':retpair}
  else:
    return {'bid':float(ret['tksbid']), 'ask':float(ret['tksask']), 'broker':ret['tksbroker'], 'pair':retpair}

@app.route("/getTickerBt", methods=['post'])
def getTickerbt():
  pair = request.json['pair'].replace('_', '-')
  ret = GetTicker.getTickerBt(pair)['bt']
  retpair = ret['symbol'].replace('-', '_')
  if 'errormsg' in ret:
    return {'bid':'---', 'ask':'---', 'broker':'bt', 'pair':retpair}
  else:
    return {'bid':float(ret['tksbid']), 'ask':float(ret['tksask']), 'broker':ret['tksbroker'], 'pair':retpair}

@app.route("/getTickerEx", methods=['post'])
def getTickerex():
  pair = request.json['pair'].replace('_', '-')
  ret = GetTicker.getTickerEx(pair)['ex']
  retpair = ret['symbol'].replace('-', '_')
  if 'errormsg' in ret:
    return {'bid':'---', 'ask':'---', 'broker':'ex', 'pair':retpair}
  else:
    return {'bid':float(ret['tksbid']), 'ask':float(ret['tksask']), 'broker':ret['tksbroker'], 'pair':retpair}

@app.route("/getTickerLq", methods=['post'])
def getTickerlq():
  pair = request.json['pair'].replace('_', '')
  ret = GetTicker.getTickerLq(pair)['lq']
  retpair = ret['symbol'].replace('USDT', '_USDT')
  if 'errormsg' in ret:
    return {'bid':'---', 'ask':'---', 'broker':'lq', 'pair':retpair}
  else:
    return {'bid':float(ret['tksbid']), 'ask':float(ret['tksask']), 'broker':ret['tksbroker'], 'pair':retpair}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
