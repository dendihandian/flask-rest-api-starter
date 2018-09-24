from flask import Flask, jsonify, request, Response
import json

app = Flask(__name__)

global idSequence
idSequence = 3
examples = [
	{
		'id': 1,
		'stringExample': 'lorem ipsum dolor sit amet',
		'numberExample': 5000,
		'booleanExample': True,
		'floatExample': 3.14
	},
	{
		'id': 2,
		'stringExample': 'lorem ipsum dolor sit amet',
		'numberExample': 5000,
		'booleanExample': True,
		'floatExample': 3.14
	}
]

@app.route('/')
def hello_world():
	return 'Hello World!'

@app.route('/api/examples')
def exampleList():
	return jsonify({
		'message': 'Example List',
		'data': examples
	}), 200

def validateExample(exampleObject):
	if 	( 'stringExample' in exampleObject and
		  'numberExample' in exampleObject and
		  'floatExample' in exampleObject and
		  'booleanExample' in exampleObject
		):
		return True
	else:
		return False

@app.route('/api/examples', methods=['POST'])
def exampleCreate():
	global idSequence
	requestData = request.get_json()
	if (validateExample(requestData)):
		newExample = {
			'id': idSequence,
			'stringExample': requestData['stringExample'],
			'numberExample': requestData['numberExample'],
			'floatExample': requestData['floatExample'],
			'booleanExample': requestData['booleanExample']
		}
		examples.insert(0, newExample)
		idSequence = idSequence + 1
		return Response(json.dumps({
			'message': 'Example Created',
			'data' : newExample
		}), 201, mimetype='application/json')

	else:
		return Response(json.dumps({
			'message': 'Bad Request'
		}), 400, mimetype='application/json')

@app.route('/api/examples/<int:exampleId>')
def exampleDetail(exampleId):
	foundExample = {}
	for example in examples:
		if example['id'] == exampleId:
			foundExample = example
			break

	return jsonify({
		'message': 'Example Detail',
		'data': foundExample
	}), 200

app.run(port=5000)
