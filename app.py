from flask import Flask, jsonify
from  flask import  request

app = Flask(__name__)

data = [
        {
            "id": 1,
            "library": "Pandas",
            "language": "Python"
        },
        {
            "id": 2,
            "library": "requests",
            "language": "Python"
        },
        {
            "id": 3,
            "library": "NumPy",
            "language": "Python"
        }
    ]

@app.route('/')
def hello():
    return "Hello Billionaire"


@app.route('/get_question_by_id', methods=['GET'])
def get_api():
    # if key doesn't exist, returns None
    question_id = request.args.get('question_id')

    return '''<h1>The question_id value is: {}</h1>'''.format(question_id)

if __name__ == "__main__":
    app.run(debug=False)