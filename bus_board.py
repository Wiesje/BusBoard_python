from flask import Flask
import requests
app = Flask(__name__)


@app.route('/<string:postcode>')
def hello_world(postcode):
    response = requests.get(f"http://api.postcodes.io/postcodes/{postcode}")
    latitude = response.json()["result"]["latitude"]
    longitude = response.json()["result"]["longitude"]
    stops = requests.get(f"https://api.tfl.gov.uk/StopPoint?stopTypes=NaptanPublicBusCoachTram&lat={latitude}&lon={longitude}")
    return stops.json()
if __name__ == "__main__": app.run()