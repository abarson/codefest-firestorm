from watson_developer_cloud import ToneAnalyzerV3
import json

class ToneAnalysis():
    def __init__(self):
        self.url = "https://gateway.watsonplatform.net/tone-analyzer/api"
        self.username = "3fffce10-8ba2-437c-a31b-2a73204ac962"
        self.password = "eD4FtUDKYaQE"
        self.tone_analyzer = ToneAnalyzerV3(
                username=self.username,
                password=self.password,
                version='2017-09-26')

    def analyze_tone(self, utterance):
        json_utterance = [{'text': utterance}]
        print(json.dumps(self.tone_analyzer.tone_chat(json_utterance), indent=2))
    

toneCheck = ToneAnalysis()

example_sentence = "Why is A.G. Jeff Sessions asking the Inspector General to investigate potentially massive FISA abuse. Will take forever, has no prosecutorial power and already late with reports on Comey etc. Isn’t the I.G. an Obama guy? Why not use Justice Department lawyers? DISGRACEFUL!"

toneCheck.analyze_tone(example_sentence)


