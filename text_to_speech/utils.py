import os

import azure.cognitiveservices.speech as speechsdk
from azure.cognitiveservices.speech import AudioDataStream
from dotenv import load_dotenv


load_dotenv()
# from text_to_speech.config import speech_config
speech_config = speechsdk.SpeechConfig(subscription=os.environ['SPEECH_RECOGNITION_KEY'], region='eastus')

# The language of the voice that speaks.
speech_config.speech_synthesis_voice_name = 'uz-UZ-SardorNeural'  # uz-UZ-MadinaNeural
speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=None)


def convert_to_audio(text: str) -> None:
    speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()
    stream = AudioDataStream(speech_synthesis_result)
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


convert_to_audio('Bugun turdim')
