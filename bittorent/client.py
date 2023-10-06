import asyncio, aiohttp, bencodepy, sys

from . import bencoding

def read_torrent(torrent_file):
    with open(torrent_file, 'rb') as file:
        torrent_data = bencodepy.decode(file.read())
    return torrent_data

async def get_peers(torrent):
        async with aiohttp.ClientSession() as session:
            resp = await session.get(torrent[b'announce'].decode(), params={
                'info_hash': torrent[b'info'][b'pieces'],
                'peer_id': '-PC0001-' + '123456789012',
                'port': 6881,
                'uploaded': 0,
                'downloaded': 0,
                'left': torrent[b'info'][b'length'],
                'compact': 1,
                'event': 'started'
            })
            resp_data = await response.read()
            peers = bencodepy.decode(resp_data)[b'peers']
            return peers

async def download(torrent_file):
    # Read and parse ".torrent" file
    torrent = read_torrent(torrent_file)
    print(torrent)

    # Get peers list from tracker in ".torrent" file
    peer_addresses = await get_peers(torrent)
    print("peer_addresses", peer_addresses)

    # # Queue for storing downloaded file pieces
    # file_pieces_queue = asyncio.Queue()

    # # Object to coordinate writing file to disk
    # file_saver = FileSaver(file_pieces_queue)

    # # Object to track peer communication/state
    # peers = [Peer(addr, file_pieces_queue) for addr in peer_addresses]

    # # Wait for all download coroutines to finish
    # await asyncio.gather(
    #     *[peer.download() for peer in peers] + # Producers
    #      [file_saver.start()]                   # Consumers
    # )

def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(download(sys.argv[1]))
    loop.close()