from flask import Flask, render_template, json, jsonify
from src.pdfupload import PDFUpload

app = Flask(__name__)
pdfupload = PDFUpload()

@app.route('/')
def root():
    salida = pdfupload.Status()
    
    if salida == 'OK':
        with open('./data/status.json') as f:
            data = json.load(f)
            response = app.response_class(response=json.dumps(data), status=200, mimetype='application/json')
    else:
        data = '{"value":"Notfound"}'
        response = app.response_class(response=data, status=200, mimetype='application/json')

    return response

@app.route('/status')
def status():
    salida = pdfupload.Status()
    
    if salida == 'OK':
        with open('./data/status.json') as f:
            data = json.load(f)
            response = app.response_class(response=json.dumps(data), status=200, mimetype='application/json')
    else:
        data = '{"value":"Notfound"}'
        response = app.response_class(response=data, status=200, mimetype='application/json')

    return response

@app.route('/isuser/<user>')
def IsUser(user):
    salida = pdfupload.IsUser(user)

    if isinstance(salida, bool):
        data = '{"value":"Notfound"}'
        response = app.response_class(response=data, status=200, mimetype='application/json')
    else:
        data = jsonify(salida)
        response = data

    return response

@app.route('/isfile/<user>/<f>')
def IsFile(user, f):
    salida = pdfupload.IsFile(user, f)

    if isinstance(salida, bool):
        data = '{"value":"Notfound"}'
        response = app.response_class(response=data, status=200, mimetype='application/json')
    else:
        data = jsonify(salida)
        response = data

    return response

@app.route('/searchfile/<user>/<f>')
def SearchFile(user, f):
    salida = pdfupload.SearchFile(user, f)

    if isinstance(salida, bool):
        data = '{"value":"Notfound"}'
        response = app.response_class(response=data,status=200,mimetype='application/json')
    else:
        data = jsonify(salida)
        response = data

    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=False)