# import os
#
# from google.auth.transport.requests import Request
# from google.oauth2 import credentials
# from google_auth_oauthlib.flow import InstalledAppFlow
# from googleapiclient import discovery
#
#
# creds = None
# SCOPES = 'https://www.googleapis.com/auth/youtube.force-ssl'
# TOKENS = 'storage.json'
#
# if os.path.exists(TOKENS):
#     creds = credentials.Credentials.from_authorized_user_file(TOKENS)
#
# if not (creds and creds.valid):
#     if creds and creds.expired and creds.refresh_token:
#         creds.refresh(Request())
#     else:
#         flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
#         creds = flow.run_local_server()
#
# with open(TOKENS, 'w') as token:
#     token.write(creds.to_json())
#
# YOUTUBE = discovery.build('youtube', 'v3', credentials=creds)
#
#
# def process(vid):
#     caption_info = YOUTUBE.captions().list(part='id',
#             videoId=vid).execute().get('items', [])
#     print(YOUTUBE.captions().list(part='id',
#             videoId=vid).execute())
#     caption_str = YOUTUBE.captions().download(id=caption_info[0]['id'],
#             tfmt='srt').execute().decode('utf-8')
#     caption_data = caption_str.split('\n\n')
#     for line in caption_data:
#         if line.count('\n') > 1:
#             i, timecode, caption = line.split('\n', 2)
#             print('%02d) [%s] %s' % (int(i), timecode, ' '.join(caption.split())))
#
#
# if __name__ == '__main__':
#     vid = '3J9jSDLFndo'
#     process(vid)
import json
import re
from pprint import pprint

import requests
import xmltodict

xml = requests.get('https://www.youtube.com/watch?v=3J9jSDLFndo').text

match = re.search(r'\{"captionTracks":(\[.*?\]),', xml)
if match is None:
    raise ValueError('Could not parse caption tracks')

match = match.group(0).rstrip(',') + '}'
data = json.loads(match)

pprint(data)
url, language_code = data['captionTracks'][0]['baseUrl'], data['captionTracks'][0]['languageCode']

captions_xml = requests.get(url).text
captions_data = xmltodict.parse(captions_xml, disable_entities=False)
pprint(captions_data)
