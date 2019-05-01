import vlc
from gmusicapi import Mobileclient


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
