
from sintax import parser
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)  # Aplica CORS a toda la aplicación

@app.route('/')

def start():
    return render_template('index.html')


@app.route('/codecraft', methods=['POST'])
def main(): 
   
    content = request.json['content']
    return json.dumps(parser.parse(content))



if __name__ == '__main__':
    app.run(debug=True)
