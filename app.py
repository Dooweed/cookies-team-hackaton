from timeit import default_timer

from dotenv import load_dotenv
from flask import Flask, send_from_directory
from flask import request
from flask_cors import CORS

from text_to_speech.utils import convert_to_audio
from translation.utils import translate
from youtube.main import get_captions

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
def index():  # put application's code here
    return send_from_directory('website', 'index.html')


@app.route('/api/transcript')
def transcript():
    url = request.args.get('link', None)
    if not url:
        return {'error': 'Add link'}
    captions, from_language = get_captions(url)
    captions = translate(captions, from_language)

    start = default_timer()
    for caption in captions:
        caption['audio'] = convert_to_audio(caption['text'])
    print(f'Overall for audio translation: {default_timer() - start}s')

    return captions


@app.route('/css/<string:filename>')
def static_css(*, filename):
    return send_from_directory('website/css', filename)


@app.route('/js/<string:filename>')
def static_js(*, filename):
    return send_from_directory('website/js', filename)


@app.route('/images/<string:filename>')
def static_images(*, filename):
    return send_from_directory('website/images', filename)


if __name__ == '__main__':
    load_dotenv()
    app.run()
