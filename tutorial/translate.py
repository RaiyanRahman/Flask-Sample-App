import json
import requests
from flask import current_app
from flask_babel import _


def translate(text, source_language, dest_language):
    if 'TRANSLATOR_KEY' not in current_app.config or \
            not current_app.config['TRANSLATOR_KEY']:
        return _('Error: the translation service is not configured.')
    auth = {'Ocp-Apim-Subscription-Key': current_app.config['TRANSLATOR_KEY']}
    r = requests.get('https://translate.yandex.net/api/v1.5/tr.json/translate'
                     '?key={}&text={}&lang={}-{}'.format(
                         current_app.config['TRANSLATOR_KEY'],
                         text, source_language, dest_language),
                     headers=auth)
    if r.status_code != 200:
        return _('Error: the translation service failed.')
    translated_text = json.loads(r.content.decode('utf-8-sig'))
    return translated_text['text'][0]
