import pickle
import flask
from flask import Flask, request, jsonify, abort

app = Flask(__name__)

# Load the model
# model_buyer = pickle.load(open('models/english_model.pkl', 'rb'))

@app.route('/spanish', methods=['GET', 'POST'])
def hello():
    resp = flask.Response("""{"Foo bar baz":"AS"}""")
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=True)