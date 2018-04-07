from watson_developer_cloud import ToneAnalyzerV3
import json

url = "https://gateway.watsonplatform.net/tone-analyzer/api"
username = "3fffce10-8ba2-437c-a31b-2a73204ac962"
password = "eD4FtUDKYaQE"

tone_analyzer = ToneAnalyzerV3(
    username=username,
    password=password,
    version='2017-09-26')

print("\ntone_chat() example 1:\n")
utterances = [{'text': 'I am very happy.', 'user': 'glenn'},
              {'text': 'It is a good day.', 'user': 'glenn'}]
print(json.dumps(tone_analyzer.tone_chat(utterances), indent=2))


