import signal
import os

from snowboy import snowboydecoder
import speech_recognition as sr

import activities

interrupted = False

model = 'snowboy/resources/kefirchik.pmdl'


def audioRecorderCallback(fname):
    print("converting audio to text")
    r = sr.Recognizer()
    with sr.AudioFile(fname) as source:
        audio = r.record(source)
    try:
        text = r.recognize_google(audio)
        words = text.split(' ')
        print(words)
        if 'exit' in words:
            exit_handler(None, None)
        if 'song' in words or 'music' in words:
            activities.play_song()

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    finally:
        os.remove(fname)


def detectedCallback():
    snowboydecoder.play_audio_file()
    print('recording audio...', flush=True)


def exit_handler(signal, frame):
    global interrupted
    interrupted = True


def interrupt_callback():
    global interrupted
    return interrupted


def main():
    signal.signal(signal.SIGINT, exit_handler)

    detector = snowboydecoder.HotwordDetector(model, sensitivity=0.38)

    print('Listening... Press Ctrl+C to exit')

    detector.start(detected_callback=detectedCallback,
                   audio_recorder_callback=audioRecorderCallback,
                   interrupt_check=interrupt_callback,
                   sleep_time=0.01)

    detector.terminate()


if __name__ == '__main__':
    main()
