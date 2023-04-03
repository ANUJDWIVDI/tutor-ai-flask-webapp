from flask import Flask, render_template, request
from utils import questions, calculate_scores

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', questions=questions)


@app.route("/submit", methods=["POST"])
def submit():
    print("-- ENTER SUBMIT --")
    answers = request.form
    percentage_score = calculate_scores(answers, questions)
    print("-- QUESTION SCORE CALCULATE DONE --")
    return render_template("result.html", percentage_score=percentage_score)


@app.route('/sample')
def sample():
    percentage_score = 30
    return render_template("result.html", percentage_score=percentage_score)


if __name__ == '__main__':
    app.run(debug=True)
