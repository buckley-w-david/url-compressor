import pickle

from flask import current_app, g
from dahuffman import HuffmanCodec

def get_codec():
    if 'codec' not in g:
        with current_app.open_resource('urls.codec', 'rb') as f:
            data = pickle.load(f)
        g.codec = HuffmanCodec(data['code_table'], concat=data['concat'])
    return g.codec
