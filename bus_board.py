from flask import Flask

app = Flask(__name__)


@app.route('/<string:postcode>')
def hello_world(postcode):
    return postcode

if __name__ == "__main__": app.run()