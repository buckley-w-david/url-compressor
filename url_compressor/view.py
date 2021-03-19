import functools

from flask import (
    Blueprint, redirect, request, render_template, current_app
)

from url_compressor.form import CompressorForm
from url_compressor import codec

bp = Blueprint('view', __name__)

@bp.route('/', methods=[ 'GET' ])
def index():
    form = CompressorForm(request.form)
    return render_template('index.html', form=form)

from dahuffman import HuffmanCodec
import base64

def compress(url):
    c = codec.get_codec()
    return base64.urlsafe_b64encode(c.encode(url)).decode('utf-8')

def decompress(slug):
    c = codec.get_codec()
    return c.decode(base64.urlsafe_b64decode(slug))

from http import HTTPStatus
@bp.route('/generate', methods=['POST'])
def generate(slug=None):
    form = CompressorForm(request.form)
    if form.validate():
        return compress(form.url.data)
    else:
        return 'You suck!', HTTPStatus.BAD_REQUEST

@bp.route('/<slug>')
def lookup(slug=None):
    try:
        url = decompress(slug)
        return redirect(url)
    except:
        return 'You suck!', HTTPStatus.NOT_FOUND
