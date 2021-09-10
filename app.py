from flask import Flask, render_template, request, redirect
import speech_recognition as sr
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])

def index():
    transcript = ""
    if request.method == "POST":

        if "file" not in request.files:
            return redirect(request.url)

        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)

        if file:
            recon = sr.Recognizer()
            audio = sr.AudioFile(file)

            with audio as source:
                data = recon.record(source)
                transcript = recon.recognize_google(data)
            print(transcript)








    return render_template("index.html", transcript=transcript)


if __name__ == "__main__":
    app.run(debug=True, threaded=True)





