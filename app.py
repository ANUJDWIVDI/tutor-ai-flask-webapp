from flask import Flask, render_template, request, redirect, url_for
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
    return redirect(url_for('result', percentage_score=percentage_score))

@app.route('/result/<int:percentage_score>')
def result(percentage_score):
    if percentage_score >= 80:
        level = 'level-5'
        print(level)
        return render_template(f'levels/level-5.html')
    elif percentage_score >= 60:
        level = 'level-4'
        print(level)
        return render_template(f'levels/level-4.html')
    elif percentage_score >= 40:
        level = 'level-3'
        print(level)
        return render_template(f'levels/level-3.html')
    elif percentage_score >= 20:
        level = 'level-2'
        print(level)
        return render_template(f'levels/level-2.html')
    else:
        level = 'level-1'
        print(level)
        return render_template(f'levels/level-1.html')


@app.route('/blog_1')
def blog_1():
    # Code to render the blog 1 template goes here
    return render_template('blog_1.html')

@app.route('/blog_1')
def blog_2():
    # Code to render the blog 1 template goes here
    return render_template('blog_1.html')

@app.route('/blog_1')
def blog_3():
    # Code to render the blog 1 template goes here
    return render_template('blog_1.html')

@app.route('/blog_1')
def blog_4():
    # Code to render the blog 1 template goes here
    return render_template('blog_1.html')

@app.route('/blog_1')
def blog_5():
    # Code to render the blog 1 template goes here
    return render_template('blog_1.html')





if __name__ == '__main__':
    app.run(debug=True)
