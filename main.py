from pathlib import Path

from dotenv import load_dotenv


def main():
    from translation.utils import translate

    from text_to_speech.config import SPEECH_FILENAME
    from text_to_speech.utils import convert_to_audio

    raw_text = 'Some text to be translated'
    text = translate(raw_text, 'en')
    print(f'Translation: {text}')

    convert_to_audio(text)
    print(f'File?: {Path(SPEECH_FILENAME).exists()}')


if __name__ == '__main__':
    load_dotenv('.env')
    main()
