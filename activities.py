import datetime

import vlc
import webbrowser
from gmusicapi import Mobileclient

from speak import say


def play_song():
    """
    Need OAuth creds first:
    from gmusicapi import Mobileclient
    api = Mobileclient()
    api.perform_oauth()
    # do instructions, it will save creds to storage.
    """
    api = Mobileclient()
    api.oauth_login(Mobileclient.FROM_MAC_ADDRESS)
    library = api.get_all_songs()
    track_id = library[0]['id']
    url = api.get_stream_url(track_id)
    p = vlc.MediaPlayer(url)
    p.play()


def open_website(domain):
    print(domain)
    url = 'https://' + domain
    webbrowser.open(url)
    print('The website you have requested has been opened for you Sir.')


def time():
    now = datetime.datetime.now()
    say('Current time is %d hours %d minutes' % (now.hour, now.minute))
