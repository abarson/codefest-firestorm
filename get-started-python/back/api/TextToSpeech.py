from watson_developer_cloud import TextToSpeechV1
import json
import pyaudio 
import requests
from __future__ import print_function

class TextToSpeech():

	def __init__(self, user, password, voice = 'en-US_AllisonVoice',
                 url = 'https://stream.watsonplatform.net/text-to-speech/api', 
                 chunk = 2048):
		self.user = "3fffce10-8ba2-437c-a31b-2a73204ac962"
		self.password = "eD4FtUDKYaQE"
		self.voice = voice
		self.url = url
		self.chunk = int(chunk)


text_to_speech = TextToSpeechV1(self.user, self.password)

