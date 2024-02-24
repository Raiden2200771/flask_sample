from flask import Flask

app = Flask(__name__)

# ルーティング
@app.route('/')
def hello_world():
    return '<h1>ハローワールド</h1>'

if __name__ == '__main__':
    app.run()