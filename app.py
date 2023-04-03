from flask import Flask, render_template, request
from utils import questions, calculate_scores

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', questions=questions)


@app.route("/submit", methods=["POST"])
def submit():
    answers = request.form
    question_scores = calculate_scores(answers, questions)
    total_points_possible = sum([sum(option["scores"]) for question in questions for option in question["options"]])
    total_score = question_scores["total_score"]
    percentage_score = (total_score / total_points_possible) * 100
    return render_template("result.html", percentage_score=percentage_score)

@app.route('/sample')
def sample():
    percentage_score= 30
    return render_template("result.html", percentage_score=percentage_score)

if __name__ == '__main__':
    app.run(debug=True)
