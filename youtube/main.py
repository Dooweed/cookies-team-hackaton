import html
import json
import re
from pprint import pprint

import requests
import xmltodict


def get_captions(url: str):
    xml = requests.get(url).text

    match = re.search(r'\{"captionTracks":(\[.*?\]),', xml)
    if match is None:
        raise ValueError('Could not parse caption tracks')

    match = match.group(0).rstrip(',') + '}'
    data = json.loads(match)

    for track in data['captionTracks']:
        if track['languageCode'] == 'en':
            url, language_code = track['baseUrl'], track['languageCode']
            break
    else:
        url, language_code = data['captionTracks'][0]['baseUrl'], data['captionTracks'][0]['languageCode']

    captions_xml = requests.get(url).text
    captions_data = xmltodict.parse(captions_xml, disable_entities=False)['transcript']['text']
    for cap in captions_data:
        text, dur, start = cap.pop('#text'), cap.pop('@dur'), cap.pop('@start')
        cap['text'] = html.unescape(text)
        cap['dur'] = float(dur)
        cap['start'] = float(start)

    return captions_data, language_code
