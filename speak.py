import os

import requests

from snowboy import snowboydecoder


def say(text):
    source = 'http://rabbit:5002/api/tts'
    r = requests.get(source, params={'text': text})
    filename = 'say_file.wav'
    open(filename, 'wb').write(r.content)
    snowboydecoder.play_audio_file(filename)
    os.remove(filename)
