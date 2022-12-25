import json
from timeit import default_timer

import requests

from translation.config import constructed_url, headers


def translate(captions: list, from_language: str, to_languages: list[str] = None):
    if to_languages is None:
        to_languages = ['uz']

    params = {
        'api-version': '3.0',
        'from': from_language,
        'to': to_languages
    }

    body = []
    for cap in captions:
        body.append({'text': cap['text']})

    start = default_timer()
    response = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = response.json()
    print(default_timer() - start)

    for i, cap in enumerate(captions):
        cap['text'] = response[i]['translations'][0]['text']

    # text = response[0]['translations'][0]['text']

    # print(json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))
    print('translated', captions)
    return captions


# print(translate('because we truly believe that this topic', 'en'))
