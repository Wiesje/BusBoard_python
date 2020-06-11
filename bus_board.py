from flask import Flask
import requests
app = Flask(__name__)


@app.route('/<string:postcode>')
def hello_world(postcode):
    response = requests.get(f"http://api.postcodes.io/postcodes/{postcode}")
    print(response)
    return response.json()

if __name__ == "__main__": app.run()