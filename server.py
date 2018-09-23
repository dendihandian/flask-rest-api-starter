from flask import Flask, jsonify, request

app = Flask(__name__)

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
	})

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
	requestData = request.get_json()
	if (validateExample(requestData)):
		examples.insert(0, requestData)
		return 'True'
	else:
		return 'False'

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
	})

app.run(port=5000)
