from flask import Flask, render_template, jsonify
import random
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/weather')
def get_weather():
    # Generate weather condition
    conditions = ['Sunny', 'Partly Cloudy', 'Cloudy', 'Rainy', 'Clear']
    temp = round(random.uniform(20, 35), 2)
    
    # Generate feels like temperature
    feels_like = round(temp + random.uniform(-2, 3), 2)
    
    data = {
        'temperature': temp,
        'feels_like': feels_like,
        'humidity': round(random.uniform(30, 80), 2),
        'pressure': round(random.uniform(980, 1020), 1),
        'wind_speed': round(random.uniform(5, 25), 1),
        'condition': random.choice(conditions),
        'visibility': round(random.uniform(8, 15), 1),
        'uv_index': random.randint(1, 11),
        'dew_point': round(random.uniform(15, 25), 1),
        'timestamp': datetime.now().strftime('%I:%M:%S %p'),
        'date': datetime.now().strftime('%A, %B %d, %Y')
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)