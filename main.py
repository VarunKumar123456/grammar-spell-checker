from flask import Flask, render_template, request
from app.spell_checker import SpellCorrector
from app.grammar_checker import GrammarChecker

app = Flask(__name__)

spell_checker = SpellCorrector()
grammar_checker = GrammarChecker()

@app.route("/", methods=["GET", "POST"])
def index():
    corrected_text = ""
    if request.method == "POST":
        input_text = request.form["input_text"]
        corrected_spelling = spell_checker.correct_sentence(input_text)
        corrected_text = grammar_checker.correct_sentence(corrected_spelling)
    return render_template("index.html", corrected_text=corrected_text)

if __name__ == "__main__":
    app.run(debug=True)
