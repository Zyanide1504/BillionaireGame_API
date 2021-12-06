from flask import Flask, jsonify
from  flask import  request
import  pandas as pd

app = Flask(__name__)

sheet_id = '1HEUEIZLdlPOenFE6Ah6WX0MbWPajd5n6KLl-sQcJW5k'
sheet_name = 'Zai-game-question'
url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}'



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


@app.route('/get_question_by_id', methods=['GET'],endpoint='func1')
def get_api():
    # if key doesn't exist, returns None
    question_id = request.args.get('question_id')

    df = pd.read_csv(url)

    df = df[df["question_ID"]==question_id]
    return df.to_json(orient="records")

@app.route('/get_all_questionID', methods=['GET'], endpoint='func2')
def get_api():
    df = pd.read_csv(url)
    df = df[["question_ID","score"]]
    return  df.to_json(orient="records")



if __name__ == "__main__":
    app.run(debug=False)