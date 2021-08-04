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
        retTickers['bi'] = {'error' : 'httperror', 'tksbroker': 'bi', 'errormsg': str(e).replace("'", '') }

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
        retTickers['fx'] = {'error' : 'httperror', 'tksbroker': 'fx', 'errormsg': str(e).replace("'", '') }

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
        retTickers['kc'] = {'error' : 'httperror', 'tksbroker': 'kc', 'errormsg': str(e).replace("'", '') }

    # エラー判定
    if 'errormsg' in retTickers['kc']:
        print('aaaaa-getTiccker(kc): errormsg:	{0}'.format(retTickers['kc']['errormsg']))

    return retTickers

def getTickerBs(pair=None, retTickers=None):
    if retTickers is None: retTickers = {}
    endpoint = 'https://www.bitstamp.net'
    method = '/api/v2/ticker'
    # https://www.bitstamp.net/api/v2/ticker/btcusdt/
    # https://www.bitstamp.net/api/v2/ticker/ethusdt/
    # https://www.bitstamp.net/api/v2/ticker/xrpusdt/
    ###### https://www.bitstamp.net/api/v2/ticker/bnbusdt/

    try:
        if pair is None:
            raise Exception('argment is none not supported!!!')
        else:
            ret = requests.get(endpoint+method + '/'+pair+'/', timeout=5)
            resdict = json.loads(ret.text)
            if ((('ask' in resdict) == True) and (('bid' in resdict) == True)):
                retTickers['bs'] = {'tksbroker' : 'bs', 'tksbid' : float(resdict['bid']), 'tksask' : float(resdict['ask']), 'symbol':pair}
            else:
                retTickers['bs'] = {'tksbroker' : 'bs', 'errormsg' : str(resdict).replace("'", ''), 'symbol':pair}
    except urllib.error.HTTPError as e:
        retTickers['bs'] = {'error' : 'httperror', 'tksbroker': 'bs', 'tkserrcode' : e.code, 'errormsg': str(e).replace("'", '') }
    except Exception as e:
        retTickers['bs'] = {'error' : 'httperror', 'tksbroker': 'bs', 'errormsg': str(e).replace("'", '') }

    # エラー判定
    if 'errormsg' in retTickers['bs']:
        print('aaaaa-getTiccker(bs): errormsg:	{0}'.format(retTickers['bs']['errormsg']))

    return retTickers

# Poloniex
def getTickerPn(pair=None, retTickers=None):
    if retTickers is None: retTickers = {}
    endpoint = 'https://poloniex.com/public'
    method = '?command=returnTicker'
    # USDT_BTC
    # USDT_ETH
    # USDT_XRP
    # USDT_BNB
    ###### https://www.bitstamp.net/api/v2/ticker/bnbusdt/

    try:
        if pair is None:
            ret = requests.get(endpoint+method, timeout=30)
            retres = [item for item in json.loads(ret.text) if item in ('USDT_BTC','USDT_ETH','USDT_XRP','USDT_BNB')]
            tmpret = {}
            for item in retres:
                tmpret[item['symbol']] = {'tksbid':float(item['bestBid']), 'tksask':float(item['bestAsk']), 'symbol':item['name']}
            retTickers['kc'] = tmpret
        else:
            ret = requests.get(endpoint+method, timeout=30)
            resdict = json.loads(ret.text)
            if (((pair in resdict) == True) and (('lowestAsk' in resdict[pair]) == True) and (('highestBid' in resdict[pair]) == True)):
                retTickers['pn'] = {'tksbroker' : 'pn', 'tksbid' : float(resdict[pair]['highestBid']), 'tksask' : float(resdict[pair]['lowestAsk']), 'symbol':pair}
            else:
                retTickers['pn'] = {'tksbroker' : 'pn', 'errormsg' : str(resdict).replace("'", ''), 'symbol':pair}
    except urllib.error.HTTPError as e:
        retTickers['pn'] = {'error' : 'httperror', 'tksbroker': 'pn', 'tkserrcode' : e.code, 'errormsg': str(e).replace("'", '') }
    except Exception as e:
        retTickers['pn'] = {'error' : 'httperror', 'tksbroker': 'pn', 'errormsg': str(e).replace("'", '') }

    # エラー判定
    if 'errormsg' in retTickers['pn']:
        print('aaaaa-getTiccker(pn): errormsg:	{0}'.format(retTickers['pn']['errormsg']))

    return retTickers

def getTickerBt(pair=None, retTickers=None):
    if retTickers is None: retTickers = {}
    endpoint = 'https://api.bittrex.com/v3'
    method = '/markets/{}/ticker'
    # https://api.bittrex.com/v3/markets/tickers
    # https://api.bittrex.com/v3/markets/BTC-USDT/ticker
    # https://api.bittrex.com/v3/markets/ETH-USDT/ticker
    # https://api.bittrex.com/v3/markets/XRP-USDT/ticker
    ###### https://api.bittrex.com/v3/markets/BNB-USDT/ticker

    try:
        if pair is None:
            ret = requests.get(endpoint+'/markets/tickers', timeout=30)
            retres = [item for item in json.loads(ret.text) if item['symbol'] in ('BTC-USDT','ETH-USDT','XRP-USDT','BNB-USDT')]
            tmpret = {}
            for item in retres:
                tmpret[item['symbol']] = {'tksbid':float(item['bestBid']), 'tksask':float(item['bestAsk']), 'symbol':item['symbol']}
            retTickers['bt'] = tmpret
        else:
            ret = requests.get((endpoint+method).format(pair), timeout=5)
            resdict = json.loads(ret.text)
            if ((('bidRate' in resdict) == True) and (('askRate' in resdict) == True)):
                retTickers['bt'] = {'tksbroker' : 'bt', 'tksbid' : float(resdict['bidRate']), 'tksask' : float(resdict['askRate']), 'symbol':resdict['symbol']}
            else:
                retTickers['bt'] = {'tksbroker' : 'bt', 'errormsg' : str(resdict).replace("'", ''), 'symbol':pair}
    except urllib.error.HTTPError as e:
        retTickers['bt'] = {'error' : 'httperror', 'tksbroker': 'bt', 'tkserrcode' : e.code, 'errormsg': str(e).replace("'", '') }
    except Exception as e:
        retTickers['bt'] = {'error' : 'httperror', 'tksbroker': 'bt', 'errormsg': str(e).replace("'", '') }

    # エラー判定
    if 'errormsg' in retTickers['bt']:
        print('aaaaa-getTiccker(bt): errormsg:	{0}'.format(retTickers['bt']['errormsg']))

    return retTickers

def getTickerEx(pair=None, retTickers=None):
    if retTickers is None: retTickers = {}
    endpoint = 'https://www.okex.com'
    method = '/api/spot/v3/instruments/{}/ticker'
    # https://www.okex.com/api/spot/v3/instruments/ticker
    # https://www.okex.com/api/spot/v3/instruments/BTC-USDT/ticker
    # https://www.okex.com/api/spot/v3/instruments/ETH-USDT/ticker
    # https://www.okex.com/api/spot/v3/instruments/XRP-USDT/ticker
    ###### https://www.okex.com/api/spot/v3/instruments/BNB-USDT/ticker

    try:
        if pair is None:
            ret = requests.get(endpoint+'/api/spot/v3/instruments/ticker', timeout=30)
            retres = [item for item in json.loads(ret.text) if item['product_id'] in ('BTC-USDT','ETH-USDT','XRP-USDT','BNB-USDT')]
            tmpret = {}
            for item in retres:
                tmpret[item['product_id']] = {'tksbid':float(item['best_bid']), 'tksask':float(item['best_ask']), 'symbol':item['product_id']}
            retTickers['ex'] = tmpret
        else:
            ret = requests.get((endpoint+method).format(pair), timeout=5)
            resdict = json.loads(ret.text)
            if ((('best_bid' in resdict) == True) and (('best_ask' in resdict) == True)):
                retTickers['ex'] = {'tksbroker' : 'ex', 'tksbid' : float(resdict['best_bid']), 'tksask' : float(resdict['best_ask']), 'symbol':resdict['product_id']}
            else:
                retTickers['ex'] = {'tksbroker' : 'ex', 'errormsg' : str(resdict).replace("'", ''), 'symbol':pair}
    except urllib.error.HTTPError as e:
        retTickers['ex'] = {'error' : 'httperror', 'tksbroker': 'ex', 'tkserrcode' : e.code, 'errormsg': str(e).replace("'", '') }
    except Exception as e:
        retTickers['ex'] = {'error' : 'httperror', 'tksbroker': 'ex', 'errormsg': str(e).replace("'", '') }

    # エラー判定
    if 'errormsg' in retTickers['ex']:
        print('aaaaa-getTiccker(ex): errormsg:	{0}'.format(retTickers['ex']['errormsg']))

    return retTickers

def getTickerLq(pair=None, retTickers=None):
    if retTickers is None: retTickers = {}
    endpoint = 'https://api.liquid.com'
    method = '/products'
    # https://www.okex.com/api/spot/v3/instruments/ticker
    # https://www.okex.com/api/spot/v3/instruments/BTC-USDT/ticker
    # https://www.okex.com/api/spot/v3/instruments/ETH-USDT/ticker
    # https://www.okex.com/api/spot/v3/instruments/XRP-USDT/ticker
    ###### https://www.okex.com/api/spot/v3/instruments/BNB-USDT/ticker

    try:
        if pair is None:
            ret = requests.get(endpoint+method, timeout=30)
            retres = [item for item in json.loads(ret.text) if item['currency_pair_code'] in ('BTCUSDT','ETHUSDT','XRPUSDT','BNBUSDT')]
            tmpret = {}
            for item in retres:
                tmpret[item['currency_pair_code']] = {'tksbid':float(item['market_bid']), 'tksask':float(item['market_ask']), 'symbol':item['currency_pair_code']}
            retTickers['lq'] = tmpret
        else:
            id = '/624' if pair=='BTCUSDT' else '/625' if pair=='ETHUSDT' else ''
            if id == '': return {'tksbid':'---', 'tksask':'---'}
            ret = requests.get(endpoint + method + id, timeout=5)
            resdict = json.loads(ret.text)
            if ((('market_bid' in resdict) == True) and (('market_ask' in resdict) == True)):
                retTickers['lq'] = {'tksbroker' : 'lq', 'tksbid' : float(resdict['market_bid']), 'tksask' : float(resdict['market_ask']), 'symbol':resdict['currency_pair_code']}
            else:
                retTickers['lq'] = {'tksbroker' : 'lq', 'errormsg' : str(resdict).replace("'", ''), 'symbol':pair}
    except urllib.error.HTTPError as e:
        retTickers['lq'] = {'error' : 'httperror', 'tksbroker': 'lq', 'tkserrcode' : e.code, 'errormsg': str(e).replace("'", '') }
    except Exception as e:
        retTickers['lq'] = {'error' : 'httperror', 'tksbroker': 'lq', 'errormsg': str(e).replace("'", '') }

    # エラー判定
    if 'errormsg' in retTickers['lq']:
        print('aaaaa-getTiccker(lq): errormsg:	{0}'.format(retTickers['lq']['errormsg']))

    return retTickers
