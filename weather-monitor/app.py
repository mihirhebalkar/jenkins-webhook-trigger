from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def index():
    data = {
        'temperature': round(random.uniform(20, 35), 2),
        'humidity': round(random.uniform(30, 80), 2)
    }
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
