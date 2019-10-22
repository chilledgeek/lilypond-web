from flask import Flask, request, render_template, send_file
from config import Config

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def my_form():
    return render_template("home.html")


@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['lilypond_text']

    with open("/Users/ec/Documents/alpine-lilypond/workdir/test.txt", "w") as f:
        f.write(text)
    f.close()

    return send_file('/Users/ec/Documents/alpine-lilypond/workdir/test.txt', attachment_filename='test_output.pdf')


if __name__ == "__main__":
    app.run()
