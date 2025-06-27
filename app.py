from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/location', methods=['POST'])
def location():
    data = request.get_json()
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    print(f"User Location: Latitude={latitude}, Longitude={longitude}")
    return {'status': 'success', 'message': 'Location received'}

if __name__ == '__main__':
    app.run(debug=True)