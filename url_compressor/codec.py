import pickle

from flask import current_app, g
from dahuffman import HuffmanCodec

import base64
import tldextract
from urllib.parse import urlparse

import enum

class Scheme(enum.Enum):
    HTTP = b'\x00'
    HTTPS = b'\x01'

    @staticmethod
    def from_name(s):
        return getattr(Scheme, s.upper())

    @staticmethod
    def from_value(v):
        return next(i for i in Scheme if i.value == v)

# TODO compress suffix separetly
# This isn't quite as simple as the scheme hack since there is
# no garunteed length/position in the blob. We could use some kind of marker that isn't a real TLD
# that we always append to the end of it.
#
# That way it'd look like {BYTE FOR SCHEME}{SOME NUMBER OF BYTES FOR SUFFIX}{SPECIAL MARKER}{THE REST}
#
# I guess we make the marker the "most common" suffix since it's going to be there every time
# Actually might have to make it the least common so that it can't be contained within any others
# Need to research markers in binary streams
# Could also have a field specifying the length of the suffix {SCHEME}{LENGTH}{LENGTH BYTES}{THE REST}
# Would need to mandate a max length since the length field would need to be a static size
class Codec:
    def __init__(self, other, suffix):
        self.other = other
        self.suffix = suffix

    def encode_url(self, url):
        parsed = urlparse(url)
        the_rest = parsed.geturl().replace('http://', '').replace('https://', '')

        b = Scheme.from_name(parsed.scheme).value
        b += self.other.encode(the_rest)
        return base64.urlsafe_b64encode(b).decode('utf-8')

    def decode_slug(self, slug):
        b = base64.urlsafe_b64decode(slug)
        scheme = Scheme.from_value(b[0:1]).name.lower()
        other = self.other.decode(b[1:])

        return f'{scheme}://{other}'

def get_codec():
    if 'codec' not in g:
        with current_app.open_resource('other.codec', 'rb') as f:
            data = pickle.load(f)
        other_codec = HuffmanCodec(data['code_table'], concat=data['concat'])
        with current_app.open_resource('suffix.codec', 'rb') as f:
            data = pickle.load(f)
        suffix_codec = HuffmanCodec(data['code_table'], concat=data['concat'])
        g.codec = Codec(other_codec, suffix_codec)
    return g.codec
