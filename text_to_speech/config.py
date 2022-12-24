import os

import azure.cognitiveservices.speech as speechsdk

SPEECH_FILENAME = 'temp.wav'

speech_config = speechsdk.SpeechConfig(subscription=os.environ['SPEECH_RECOGNITION_KEY'], region='eastus')

# The language of the voice that speaks.
speech_config.speech_synthesis_voice_name = 'uz-UZ-SardorNeural'  # uz-UZ-MadinaNeural
