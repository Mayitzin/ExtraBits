"""
Test yandex
https://translate.yandex.com/developers/keys
"""
print "Testing Yandex"

from yandex_translate import YandexTranslate
translate = YandexTranslate('trnsl.1.1.20170808T200819Z.353052b379db306f.afbcedbaeec9d823cfac008f017161e8cb93791c')
input_text = "Hola, mundo!"
output_text = translate.translate('Hola, mundo!', 'es-en')['text'][0]
print "Translate:\n\t", output_text