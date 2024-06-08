from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Initialize the grid dictionary
grid = {}

# Function to set a value in the grid
def set_grid_value(x, y, z, value):
    grid[(x, y, z)] = value

# Function to get a value from the grid
def get_grid_value(x, y, z):
    return grid.get((x, y, z), None)  # Returns None if the coordinate is not set

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/set', methods=['POST'])
def set_value():
    data = request.json
    x = int(data['x'])
    y = int(data['y'])
    z = int(data['z'])
    value = data['value']
    set_grid_value(x, y, z, value)
    return jsonify({'status': 'success', 'message': f'Set value at ({x}, {y}, {z})'})

@app.route('/get', methods=['GET'])
def get_value():
    x = int(request.args.get('x'))
    y = int(request.args.get('y'))
    z = int(request.args.get('z'))
    value = get_grid_value(x, y, z)
    return jsonify({'x': x, 'y': y, 'z': z, 'value': value})

if __name__ == '__main__':
    app.run(debug=True)

