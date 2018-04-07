from watson_developer_cloud import ToneAnalyzerV3, LanguageTranslatorV2, VisualRecognitionV3
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions

import json


class NaturalLanguageUnderstanding():
    def __init__(self):
        self.username = "a231076a-503e-4b98-a0bd-5f99637c240f"
        self.password = "ROksYqn7v48H"
        self.url = "https://gateway.watsonplatform.net/natural-language-understanding/api"
        
        self.nlu = NaturalLanguageUnderstandingV1(username=self.username, 
                                                  password=self.password, 
                                                  version='2018-03-16')
    
    def analyze_nl(self, text):
        L = len(text.split(" "))
        response = self.nlu.analyze(text=text,
                                    features=Features(entities=EntitiesOptions(emotion=True, 
                                                                               sentiment=True, 
                                                                               limit=L),
                                                      keywords=KeywordsOptions(emotion=True, sentiment=True,
                                                                               limit=L)))

        return json.dumps(response, indent=2)

class ToneAnalysis():
    def __init__(self):
        self.url = "https://gateway.watsonplatform.net/tone-analyzer/api"
        self.username = "3fffce10-8ba2-437c-a31b-2a73204ac962"
        self.password = "eD4FtUDKYaQE"
        self.tone_analyzer = ToneAnalyzerV3(username=self.username,
                                            password=self.password,
                                            version='2017-09-26')

    def analyze_tone(self, utterance):
        json_utterance = [{'text': utterance}]
        return json.dumps(self.tone_analyzer.tone_chat(json_utterance), indent=2)


class Translator():
    def __init__(self):
        self.languages = {"English": "en", "French": "fr", "Arabic": "ar",
                          "German": "de", "Italian": "it", "Japanese": "ja",
                           "Korean": "ko", "Portuguese": "pt", "Spanish": "es"}
        self.url = "https://gateway.watsonplatform.net/language-translator/api"
        self.username = "e01c0489-3c59-4d94-a61b-75335f768528"
        self.password = "5EX02KFSpIOP"
        self.language_translator = LanguageTranslatorV2(username=self.username,
                                                        password=self.password)

    def translate(self, text, target_language):
        actual_language = self.languages[target_language]
        return self.language_translator.translate(text, source='en', target=actual_language)


class VisualRecognition():
    def __init__(self):
        self.url = "https://gateway-a.watsonplatform.net/visual-recognition/api"
        self.note = "It may take up to 5 minutes for this key to become active"
        self.api_key = "bbe846d049b62bb116e525f0ad3c6b2989d99613"
        visual_recognition = VisualRecognitionV3('2016-05-20', api_key=self.api_key)
    
    def undefined_functionality(self):
        pass

#translator = Translator()
#translator.translate('How are you?', 'chinese')

#toneCheck = ToneAnalysis()
#toneCheck.analyze_tone(example_sentence)
