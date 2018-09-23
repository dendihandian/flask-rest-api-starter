from flask import Flask, jsonify

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

@app.route('/examples')
def exampleList():
	return jsonify({'data': examples})

@app.route('/examples/<int:exampleId>')
def exampleDetail(exampleId):
	return_value = {}
	for example in examples:
		if example['id'] == exampleId:
			return_value = example
			break

	return jsonify(return_value)

app.run(port=5000)
