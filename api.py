from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_KEY = '8f7150aa7d2a401e91d222910240107'
WEATHER_API_URL = 'http://api.weatherapi.com/v1/current.json'

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({'error': 'City parameter is required'}), 400

    params = {
        'key': API_KEY,
        'q': city
    }

    response = requests.get(WEATHER_API_URL, params=params)
    if response.status_code != 200:
        return jsonify({'error': 'City not found or WeatherAPI.com error'}), 404
    
    #Retrieve data from response
    data = response.json()

    weather_info = {
        'city': data['location']['name'],
        'temperature': data['current']['temp_c'],
        'condition': data['current']['condition']['text'],
        'humidity': data['current']['humidity'],
        'wind_speed': data['current']['wind_kph'] 
   }
    
    return jsonify(weather_info), 200

if __name__ == '__main__':
    app.run(debug=True)

