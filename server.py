from flask import Flask

app = Flask(__name__)


@app.route('/')
def api_root():
	return 'wassaup man'


@app.route('/<text>')
def api_other(text):
	return f"Wassup Man. There's no route at /{text}"


@app.route('/person/<_id>')
def api_person(_id):
	return f"I don't have any information on the person with id {_id}"


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80, threaded=True)
