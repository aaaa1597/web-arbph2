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

def getTickerFx(pair):
    print('pair=' + pair)
    return {'ask' : 500.1, 'bid' : 500.3}

def getTickerKc(pair):
    print('pair=' + pair)
    return {'ask' : 500.1, 'bid' : 500.4}

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

