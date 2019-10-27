from flask import Flask, request, render_template, send_file

from app.service.file_operator import FileOperator
from app.service.score_generator import ScoreGenerator

app = Flask(__name__)
app.config.from_object(__name__)

_score_generator = ScoreGenerator.load_default()


@app.route('/')
def landing_page():
    return render_template("home.html")


@app.route('/', methods=['POST'])
def form_post(input: str = "",
              score_generator: ScoreGenerator = _score_generator,
              file_operator_factory: FileOperator = FileOperator):
    text = request.form['lilypond_text'] if not input else input

    file_operator_instance = file_operator_factory.load_default()

    output_filepath = score_generator.run(text, file_operator_instance)

    if output_filepath is None:
        return "Something wrong...please follow correct lilypond syntax for input text"
    else:
        return send_file(output_filepath,
                         attachment_filename=output_filepath.split("/")[-1],
                         conditional=True)


if __name__ == "__main__":
    app.run(port=8080,
            host="0.0.0.0")
