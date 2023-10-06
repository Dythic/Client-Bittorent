from bittorent.tracker import Tracker

class TorrentClient:

    def __init__(self, torrent):
        self.tracker = Tracker(torrent)
        self.available_peers = Queue()