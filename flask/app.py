from flask import Flask, jsonify
app = Flask(__name__)

DB = [{'name': 'Alice', 
      'email': 'alice@outlook.com'},
      {'name': 'Ben', 
      'email': 'ben@outlook.com'}]

@app.route('/api')
def index():
    return jsonify(DB[0])


if __name__ == "__main__":
    app.run(host='0.0.0.0')