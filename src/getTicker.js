function getTickerBiAndsetVal(pair, retbidrow, retaskrow) {
    pair = pair.replace('(T)', 'T');
    pair = pair.replace('/', '');
    let request = new XMLHttpRequest();
    request.open('GET', 'https://api.binance.com/api/v3/ticker/bookTicker' + '?symbol=' + pair, true);
    request.responseType = 'json';
    request.onload = function () {
        let data = this.response;
        retbidrow.textContent = parseFloat(data['bidPrice']).toString();
        retaskrow.textContent = parseFloat(data['askPrice'].toString());
    };
    request.send();
}