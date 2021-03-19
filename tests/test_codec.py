from url_compressor import create_app
from url_compressor.codec import get_codec

def test_codec(test_client):
    codec = get_codec()

    url = 'https://reddit.com'
    slug = codec.encode_url(url)
    decoded = codec.decode_slug(slug)

    print(f'url is "{url}"')
    print(f'slug is "{slug}"')
    print(f'decoded is "{decoded}"')
    assert url == decoded
