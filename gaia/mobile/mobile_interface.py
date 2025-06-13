from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('mobile_dashboard.html')

@app.route('/status', methods=['GET'])
def status():
    # Example payload, replace with live status fetch from GAIA core
    return jsonify({
        'status': 'Online',
        'mood': 'Curious',
        'tasks': ['Monitoring markets', 'Dream training'],
        'uptime': '3h 24m'
    })

@app.route('/command', methods=['POST'])
def command():
    data = request.json
    command = data.get('command', '')
    # Send command to GAIAβ€™s core engine (stub here)
    return jsonify({'received': command, 'response': 'Command acknowledged'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8888)
