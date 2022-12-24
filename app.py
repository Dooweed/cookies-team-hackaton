from dotenv import load_dotenv
from flask import Flask, send_from_directory
from flask import request

from translation.utils import translate
from youtube.main import get_captions

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return send_from_directory('website', 'index.html')


@app.route('/api/transcript')
def transcript():
    url = request.args.get('link', None)
    if not url:
        return {'error': 'Add link'}
    captions, from_language = get_captions(url)
    translate(captions, from_language)
    print('gege')
    return captions


@app.route('/css/<string:filename>')
def static_css(*, filename):
    return send_from_directory('website/css', filename)


@app.route('/js/<string:filename>')
def static_js(*, filename):
    return send_from_directory('website/js', filename)


if __name__ == '__main__':
    load_dotenv()
    app.run()
