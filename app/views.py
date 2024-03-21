from app import app
from flask import render_template, send_file, request
from app.tts import syn
import io

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/say')
def say():
    if (request.form['text'] == ''): return "No text provided"
    text = request.form['text']
    OUTPUT_FILE = "audio.wav"
    output = syn.tts(text)
    audio_out = io.BytesIO()
    syn.save_wav(output, OUTPUT_FILE)
    return send_file(audio_out, mimetype="audio/wav", as_attachment=True, download_name="audio-1.wav")