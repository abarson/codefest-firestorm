from watson_developer_cloud import TextToSpeechV1, SpeechToTextV1

class TextToSpeech():

    def __init__(self):
        self.url = "https://stream.watsonplatform.net/text-to-speech/api"
        self.username = "5536f535-ad86-4ac0-a103-252cac859247"
        self.password = "XK7mOsXEfjTO"
        self.text_to_speech = TextToSpeechV1(
            username = self.username,
            password = self.password)

    def synthesize_speech(self, text, file_out):
        with open(file_out, 'wb') as audio_file:
            audio_file.write(
                self.text_to_speech.synthesize(text, accept='audio/wav', 
                    voice="en-US_AllisonVoice").content)


class SpeechToText():

    def __init__(self):
        self.url = "https://stream.watsonplatform.net/speech-to-text/api"
        self.username = "0be86788-e98b-49f7-bf61-f631cfc5f12a"
        self.password = "e6aAIQp6nvMk"
        self.speech_to_text = SpeechToTextV1(
            username = self.username,
            password = self.password,
            url = self.url
        )

    def comprehend_speech(self, file_in):
        with open(file_in, 'rb') as audio_file:
            self.speech_to_text.recognize(
                audio_file, 
                content_type='audio/wav', 
                timestamps=True,
                word_confidence=True)
