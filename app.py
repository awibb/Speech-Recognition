from flask import Flask, render_template, request, redirect
import speech_recognition as sr
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])

def index():
    text = ""
    if request.method == "POST":
        if "file" not in request.files:
            return redirect(request.url)
        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)
        if file:
            recon = sr.Recognizer()
            audio = sr.AudioFile(file)

            with audio as stream:
                data = recon.record(stream)
                text = recon.recognize_google(data)

    return render_template("index.html", transcript=text)

if __name__ == "__main__":
    app.run(debug=True, threaded=True)