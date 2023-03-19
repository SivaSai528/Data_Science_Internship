from flask import Flask, render_template, request

app = Flask(__name__)


notes = []
@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'GET':
        return render_template("home.html")
    else:
        note = request.form.get("note")
        clear = request.form.get("clear")
        if note!="":
            notes.append(note)
        if clear=='True':
            notes.clear()
        return render_template("home.html", notes=notes)


if __name__ == '__main__':
    app.run(debug=True)