import json

import requests

from translation.config import constructed_url, headers


def translate(raw_text: str, from_language: str, to_languages: list[str] = None):
    if to_languages is None:
        to_languages = ['uz']

    params = {
        'api-version': '3.0',
        'from': from_language,
        'to': to_languages
    }

    # You can pass more than one object in body.
    body = [{
        'text': raw_text
    }]

    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()

    text = response[0]['translations'][0]['text']

    print(json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))
    return text
