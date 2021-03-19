from collections import Counter, defaultdict
import csv
import itertools
import string
import sys
from urllib.parse import urlparse

from dahuffman import HuffmanCodec
import tldextract

other = []
suffix = []
for filename in sys.argv[1:]:
    with open(filename, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            url = row['url']
            parts = urlparse(url)
            ext = tldextract.extract(url)

            other.extend(ext.domain + parts.path + parts.params + '?' + parts.query + '#' + parts.fragment)
            suffix.append(ext.suffix)

counter = Counter(other)
freq = defaultdict(int)
freq.update(counter)

# Make sure that all allowed url characters have an entry
allowed_characters = "!#$&'()*+,/:;=?@[]ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_.~"
for char in allowed_characters:
    freq[char] = freq[char]

other_codec = HuffmanCodec.from_frequencies(freq)
other_codec.save('other.codec')

counter = Counter(suffix)
freq = defaultdict(int)
freq.update(counter)

# Make sure that all tlds have an entry
# TODO
all_tlds = []
for char in all_tlds:
    freq[char] = freq[char]

suffix_codec = HuffmanCodec.from_frequencies(freq)
suffix_codec.save('suffix.codec')
