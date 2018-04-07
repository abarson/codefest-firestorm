from watson_apis import Translator

translator = Translator()

'FRENCH'
#target_language = 'french'
#target_language = 'chinese'^
#target_language = 'arabic'
#target_language = 'dutch'^
#target_language = 'german'
target_language = 'Italian'



print(translator.translate('Hey how is it going?', target_language))
