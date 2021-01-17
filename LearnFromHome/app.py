from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/learn")
def learn():
    return render_template("learn.html")


@app.route("/quiz")
def quiz():
    return render_template("quiz.html")


@app.route("/csLearn")
def csLearn():
    return render_template("csLearn.html")


@app.route("/computer_network")
def computer_network():
    return render_template("computer_network.html")


@app.route("/computer_network_quiz")
def computer_network_quiz():
    return render_template("computer_network_quiz.html")


@app.route("/osiModel")
def osiModel():
    return render_template("osiModel.html")


@app.route("/osiModelQuiz")
def osiModelQuiz():
    return render_template("osiModelQuiz.html")


@app.route("/csQuiz")
def csQuiz():
    return render_template("csQuiz.html")


if __name__ == "__main__":
    app.run(debug=True)
