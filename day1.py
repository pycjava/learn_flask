from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello 余晓东1231231 World!'

if __name__ == '__main__':
    app.debug = True
    app.run()