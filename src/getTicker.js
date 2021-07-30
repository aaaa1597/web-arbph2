function getTickerBiAndsetVal(pair, retbidrow, retaskrow) {
    /* pair = 'BTC/USD(T)' */
    const endpoint = 'https://api.binance.com/api/v3/';
    pair = pair.replace('(T)', 'T');
    pair = pair.replace('/', '');
    let request = new XMLHttpRequest();
    url = endpoint + 'ticker/bookTicker' + '?symbol=' + pair;

    fetch(url).then(res => {
        return res.json();
    }).then(data => {
       retbidrow.textContent = parseFloat(data['bidPrice']);
       retaskrow.textContent = parseFloat(data['askPrice']);
    });

//    console.log(window.myp.Pairs);
}

function getTickerFxAndsetVal(pair, retbidrow, retaskrow) {
    const urltest = 'https://randomuser.me/api/';
    fetch(urltest).then(function(response) {
        console.log('zzzzz' + response.text());
    }).then(function(text) {
        console.log('zzzzz' + text);
    });
    
    /* pair = 'BTC/USD(T)' */
    console.log('getTickerFxAndsetVal() s ' + pair);
    const endpoint = 'https://ftx.com/api/';
    pair = pair.replace('(T)', '');

    url = endpoint + 'markets/' + pair;
    fetch(url).then(function(response) {
        console.log(response.text());
    }).then(function(text) {
        console.log(text);
    }).catch(err => {
        console.log('err= ' + err);
    });

//     let request = new XMLHttpRequest();
//     console.log(endpoint + 'markets/' + pair);
//     request.open('GET', endpoint + 'markets/' + pair, true);
//     request.responseType = 'json';
//     request.onload = function () {
//         console.log('getTickerFxAndsetVal()::onload() s ' + this);
//         let data = this.response;
//         console.log(data);
// //        retbidrow.textContent = parseFloat(data['bidPrice']);
// //        retaskrow.textContent = parseFloat(data['askPrice']);
//         console.log('getTickerFxAndsetVal()::onload() e');
//     };
//     request.onerror = function(XMLHttpRequest, textStatus, errorThrown) {
//         console.log('getTickerFxAndsetVal()::onerror() s');
//         console.log(JSON.stringify(XMLHttpRequest));
//         console.log(JSON.stringify(textStatus));
//         console.log(JSON.stringify(errorThrown));
//         console.log('getTickerFxAndsetVal()::onerror() e');
//       };
//     request.send();
    console.log('send ftx');

//    console.log(window.myp.Pairs);
    console.log('getTickerFxAndsetVal() e');
}

function getTickerKcAndsetVal(pair, retbidrow, retaskrow) {
    /* pair = 'BTC/USD(T)' */
//  https://api.kucoin.com/api/v1/market/orderbook/level1?symbol=BTC-USDT
    console.log('getTickerKcAndsetVal() s ' + pair);
    endpoint = 'https://api.kucoin.com/';
    pair = pair.replace('(T)', 'T');
    pair = pair.replace('/', '-');

    let request = new XMLHttpRequest();
    request.open('GET', endpoint + 'api/v1/market/orderbook/level1?symbol=' + pair, true);
    request.responseType = 'json';
    request.onload = function () {
        let data = this.response;
        console.log('--------' + data);
//        retbidrow.textContent = parseFloat(data['bidPrice']);
//        retaskrow.textContent = parseFloat(data['askPrice']);
    };
    request.onerror = function(XMLHttpRequest, textStatus, errorThrown) {
        console.log('getTickerKcAndsetVal()::onerror() s');
        console.log(JSON.stringify(XMLHttpRequest));
        console.log(JSON.stringify(textStatus));
        console.log(JSON.stringify(errorThrown));
        console.log('getTickerKcAndsetVal()::onerror() e');
      };
    request.send();

//    console.log(window.myp.Pairs);
    console.log('getTickerKcAndsetVal() e');
}

