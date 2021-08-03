import requests
import json
import urllib

def getTickerBi(pair=None, retTickers=None):
    if retTickers is None: retTickers = {}

    try:
        if pair is None:
            biret = requests.get('https://api.binance.com/api/v3/ticker/bookTicker', timeout=30)
            retres = [item for item in json.loads(biret.text) if item['symbol'] in ('BNBUSDS','BNBUSDC','BNBPAX','BNBTUSD','BNBUSDT','USDSUSDC','USDSPAX','USDSTUSD','USDSUSDT','USDCPAX','USDCTUSD','USDCUSDT','PAXUSDT','PAXTUSD','TUSDUSDT')]
            tmpret = {}
            for item in retres:
                tmpret[item['symbol']] = {'tksbid':float(item['bidPrice']), 'tksask':float(item['askPrice']), 'symbol':item['symbol']}
            retTickers['bi'] = tmpret
        else:
            biret = requests.get('https://api.binance.com/api/v3/ticker/bookTicker?symbol=' + pair, timeout=5)
            biresdict = json.loads(biret.text)
            # {'symbol': 'BTCUSDT', 'askPrice': '3420.98000000', 'bidQty': '0.19585000', 'askQty': '0.76125500', 'bidPrice': '3419.17000000'}
            if (('askPrice' in biresdict) == True) and (('bidPrice' in biresdict) == True):
                retTickers['bi'] = {'tksbroker' : 'bi', 'tksbid' : float(biresdict['bidPrice']), 'tksask' : float(biresdict['askPrice']), 'symbol':biresdict['symbol']}
            else:
                retTickers['bi'] = {'tksbroker' : 'bi', 'errormsg' : str(biresdict).replace("'", ''), 'symbol':pair}
    except urllib.error.HTTPError as e:
        retTickers['bi'] = {'error' : 'httperror', 'tksbroker': 'bi', 'tkserrcode' : e.code, 'errormsg': str(e).replace("'", '') }
    except Exception as e:
        retTickers['bi'] = {'error' : 'httperror', 'tksbroker': 'bi', 'tkserrcode' : e.code, 'errormsg': str(e).replace("'", '') }

    # エラー判定
    if 'errormsg' in retTickers['bi']:
        print('aaaaa-getTiccker(bi): errormsg:	{0}'.format(retTickers['bi']['errormsg']))

    return retTickers

def getTickerFx(pair=None, retTickers=None):
    if retTickers is None: retTickers = {}
    endpoint = 'https://ftx.com/api'
    method = '/markets'
    # https://ftx.com/api/markets/BTC/USD
    # https://ftx.com/api/markets/BTC/USDT
    # https://ftx.com/api/markets/ETH/USD
    # https://ftx.com/api/markets/ETH/USDT
    # https://ftx.com/api/markets/XRP/USD
    # https://ftx.com/api/markets/XRP/USDT
    # https://ftx.com/api/markets/BNB/USD
    # https://ftx.com/api/markets/BNB/USDT
    try:
        if pair is None:
            ret = requests.get(endpoint+method, timeout=30)
            retres = [item for item in json.loads(ret.text) if item['symbol'] in ('BTC/USD','BTC/USDT','ETH/USD','ETH/USDT','XRP/USD','XRP/USDT','BNB/USD','BNB/USDT')]
            tmpret = {}
            for item in retres:
                tmpret[item['symbol']] = {'tksbid':float(item['bid']), 'tksask':float(item['ask']), 'symbol':item['name']}
            retTickers['fx'] = tmpret
        else:
            ret = requests.get(endpoint+method + '/'+pair, timeout=5)
            resdict = json.loads(ret.text)
            if ((('result' in resdict) == True) and (('ask' in resdict['result']) == True) and (('bid' in resdict['result']) == True)):
                retTickers['fx'] = {'tksbroker' : 'fx', 'tksbid' : float(resdict['result']['bid']), 'tksask' : float(resdict['result']['ask']), 'symbol':resdict['result']['name']}
            else:
                retTickers['fx'] = {'tksbroker' : 'fx', 'errormsg' : str(resdict).replace("'", ''), 'symbol':pair}
    except urllib.error.HTTPError as e:
        retTickers['fx'] = {'error' : 'httperror', 'tksbroker': 'fx', 'tkserrcode' : e.code, 'errormsg': str(e).replace("'", '') }
    except Exception as e:
        retTickers['fx'] = {'error' : 'httperror', 'tksbroker': 'fx', 'tkserrcode' : e.code, 'errormsg': str(e).replace("'", '') }

    # エラー判定
    if 'errormsg' in retTickers['fx']:
        print('aaaaa-getTiccker(fx): errormsg:	{0}'.format(retTickers['fx']['errormsg']))

    return retTickers

def getTickerKc(pair=None, retTickers=None):
    if retTickers is None: retTickers = {}
    endpoint = 'https://api.kucoin.com'
    method = '/api/v1/market/orderbook/level1'
    # https://api.kucoin.com/api/v1/market/orderbook/level1?symbol=BTC-USDT
    # https://api.kucoin.com/api/v1/market/orderbook/level1?symbol=ETH-USDT
    # https://api.kucoin.com/api/v1/market/orderbook/level1?symbol=XRP-USDT
    # https://api.kucoin.com/api/v1/market/orderbook/level1?symbol=BNB-USDT

    try:
        if pair is None:
            ret = requests.get(endpoint+method, timeout=30)
            retres = [item for item in json.loads(ret.text) if item['symbol'] in ('BTC-USDT','ETH-USDT','XRP-USDT','BNB-USDT')]
            tmpret = {}
            for item in retres:
                tmpret[item['symbol']] = {'tksbid':float(item['bestBid']), 'tksask':float(item['bestAsk']), 'symbol':item['name']}
            retTickers['kc'] = tmpret
        else:
            ret = requests.get(endpoint+method + '?symbol='+pair, timeout=5)
            resdict = json.loads(ret.text)
            if ((('data' in resdict) == True) and (('bestAsk' in resdict['data']) == True) and (('bestBid' in resdict['data']) == True)):
                retTickers['kc'] = {'tksbroker' : 'kc', 'tksbid' : float(resdict['data']['bestBid']), 'tksask' : float(resdict['data']['bestAsk']), 'symbol':pair}
            else:
                retTickers['kc'] = {'tksbroker' : 'kc', 'errormsg' : str(resdict).replace("'", ''), 'symbol':pair}
    except urllib.error.HTTPError as e:
        retTickers['kc'] = {'error' : 'httperror', 'tksbroker': 'kc', 'tkserrcode' : e.code, 'errormsg': str(e).replace("'", '') }
    except Exception as e:
        retTickers['kc'] = {'error' : 'httperror', 'tksbroker': 'kc', 'tkserrcode' : e.code, 'errormsg': str(e).replace("'", '') }

    # エラー判定
    if 'errormsg' in retTickers['kc']:
        print('aaaaa-getTiccker(kc): errormsg:	{0}'.format(retTickers['kc']['errormsg']))

    return retTickers

def getTickerBs(pair):
    print('pair=' + pair)
    return {'ask' : 500.1, 'bid' : 500.5}

def getTickerPn(pair):
    print('pair=' + pair)
    return {'ask' : 500.1, 'bid' : 500.6}

def getTickerBt(pair):
    print('pair=' + pair)
    return {'ask' : 500.1, 'bid' : 500.7}

def getTickerEx(pair):
    print('pair=' + pair)
    return {'ask' : 500.1, 'bid' : 500.8}

def getTickerLq(pair):
    print('pair=' + pair)
    return {'ask' : 500.1, 'bid' : 500.9}

def getTickerBb(pair):
    print('pair=' + pair)
    return {'ask' : 500.1, 'bid' : 501.0}

