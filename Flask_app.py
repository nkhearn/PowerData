
# A very simple Flask script to store the json data posted to it
# PUT and POST methods store the data 
# GET method retrieves the stored json data

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'App functioning!'

stored_data = None

@app.route('/store/', methods=['POST', 'GET'])
def store_data():
    global stored_data
    if request.method == 'POST':
        try:
            data = request.get_json()
            if data is None:
                return jsonify({"error": "Invalid JSON data"}), 400
            stored_data = jsonify(data).get_json() # Store the json object, not just the string
            return jsonify({"message": "Data stored successfully"}), 200
        except Exception as e:
            return jsonify({"error": f"An error occurred: {str(e)}"}), 400

    elif request.method == 'GET':
        if stored_data is not None:
            return jsonify(stored_data), 200
        else:
            return jsonify({"message": "No data stored yet"}), 404

#if __name__ == '__main__':
#    app.run(debug=True)
