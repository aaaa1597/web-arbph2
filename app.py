from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
  return render_template('index.html')

@app.route("/getTickerBi")
def gettickerbi():
  return {'ask' : 500.1, 'bid' : 500.2}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
