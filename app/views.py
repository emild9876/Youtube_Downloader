from app import app
from pytube import YouTube
import tkinter
from tkinter import filedialog

from flask import render_template, request, redirect, jsonify, make_response, flash

myFormats = [
    ('Audio', '*.mp3'),
    ('Video', '*.mp4')
]


@app.route("/")
def index():
    return render_template("base.html")


@app.route("/audio", methods=('GET', 'POST'))
def audio():
    if request.method == 'POST':

        YouTube_URL = request.form['Youtube URL']

        if not YouTube_URL:
            flash('Content is required!')
        else:
            audio = YouTube(YouTube_URL)
            stream = audio.streams.get_audio_only()
            stream.download(output_path=filedialog.asksaveasfilename(filetypes=myFormats, title="Save as..."), filename=audio.title.replace('?', '') + ".mp3")
    return render_template("audio.html")


@app.route("/video", methods=('GET', 'POST'))
def video():
    if request.method == 'POST':

        YouTube_URL = request.form['Youtube URL']

        if not YouTube_URL:
            flash('Content is required!')
        else:
            video = YouTube(YouTube_URL)
            stream = video.streams.get_highest_resolution()
            stream.download(output_path=filedialog.asksaveasfilename(filetypes=myFormats, title="Save as..."), filename=video.title.replace('?', '') + ".mp4")
    return render_template("video.html")




