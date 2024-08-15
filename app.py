from flask import Flask, render_template, jsonify
import run
from azure.cosmos import CosmosClient, exceptions

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, Python!'

@app.route('/read_item')
def create_item():
    try:
        result = run.run_sample()
        return render_template('result.html', result=result)
    except exceptions.CosmosHttpResponseError as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
