import base64
import os
from pathlib import Path
from pprint import pprint
from timeit import default_timer

import azure.cognitiveservices.speech as speechsdk
from azure.cognitiveservices.speech import AudioDataStream
from dotenv import load_dotenv

load_dotenv()
# from text_to_speech.config import speech_config
speech_config = speechsdk.SpeechConfig(subscription=os.environ['SPEECH_RECOGNITION_KEY'], region='eastus')

# The language of the voice that speaks.
speech_config.speech_synthesis_voice_name = 'uz-UZ-SardorNeural'  # uz-UZ-MadinaNeural
speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=None)


def convert_to_audio(text: str) -> str:
    synth_start = default_timer()
    speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()
    stream = AudioDataStream(speech_synthesis_result)
    stream.save_to_wav_file('temp.wav')
    synth = default_timer() - synth_start
    encode_start = default_timer()

    with open('temp.wav', 'rb') as file:
        encoded = base64.b64encode(file.read()).decode()

    Path('temp.wav').unlink(missing_ok=True)
    print(f'Synth: {synth}s, Convert: {default_timer() - encode_start}s')

    print('stream hehe', stream)
    if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print("Speech synthesized for text [{}]".format(text))
    elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_synthesis_result.cancellation_details
        print("Speech synthesis canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            if cancellation_details.error_details:
                print("Error details: {}".format(cancellation_details.error_details))
                print("Did you set the speech resource key and region values?")

    return encoded


convert_to_audio('Bugun turdim - Bugaga')
