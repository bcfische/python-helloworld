from flask import Flask
import json
import logging

app = Flask(__name__)

@app.route('/')
def hello():
    app.logger.info('ROOT')
    return 'Hello World!'

@app.route('/status')
def status():
    app.logger.info('STATUS')
    response = app.response_class(
        response=json.dumps({'result':'OK - healthy'}),
        status=200,
        mimetype='application/json')
    return response    

@app.route('/metrics')
def metrics():
    app.logger.info('METRICS')
    response = app.response_class(
        response=json.dumps({'data': {'UserCount': '140', 'UserCountActive': '23'}}),
        status=200,
        mimetype='application/json')
    return response

if __name__ == '__main__':
    #logging.basicConfig(filename='app.log', level=logging.DEBUG)
    app.run()
