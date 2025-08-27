from flask import Flask, render_template, request
import random

app = Flask(__name__)

def get_random_question():
    base = random.randint(2, 9)
    exponent = random.randint(2, 5)
    return base, exponent

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get previous question and user's answer
        prev_base = int(request.form["base"])
        prev_exponent = int(request.form["exponent"])
        user_answer = request.form.get("answer", "")
        correct = prev_base ** prev_exponent
        try:
            user_answer = int(user_answer)
        except ValueError:
            user_answer = None
        result = "correct" if user_answer == correct else "wrong"
        # Generate new question for next round
        base, exponent = get_random_question()
        return render_template(
            "Project.html",
            base=base,
            exponent=exponent,
            correct=correct,
            result=result,
            prev_base=prev_base,
            prev_exponent=prev_exponent
        )
    else:
        base, exponent = get_random_question()
        return render_template(
            "Project.html",
            base=base,
            exponent=exponent,
            correct=None,
            result=None,
            prev_base=None,
            prev_exponent=None
        )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)