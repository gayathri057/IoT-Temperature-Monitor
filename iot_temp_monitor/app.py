from flask import Flask, render_template, jsonify
import random
import time

app = Flask(__name__)

# Simulate temperature sensor
def get_temperature():
    return round(random.uniform(20, 35), 2)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/temperature')
def temperature():
    return jsonify({'temperature': get_temperature(), 'time': time.strftime('%H:%M:%S')})

if __name__ == '__main__':
    app.run(debug=True)
