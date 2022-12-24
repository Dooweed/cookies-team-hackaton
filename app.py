from dotenv import load_dotenv
from flask import Flask
from flask import request

from translation.utils import translate
from youtube.main import get_captions

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return 'Hello world'


@app.route('/api/transcript')
def transcript():
    url = request.args.get('link', None)
    if not url:
        return {'error': 'Add link'}
    captions, from_language = get_captions(url)
    translate(captions, from_language)
    print('gege')
    return captions


if __name__ == '__main__':
    load_dotenv()
    app.run()
