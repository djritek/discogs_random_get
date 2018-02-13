#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import random
import json
import urllib
import requests
from requests_oauthlib import OAuth1
from requests_oauthlib import OAuth1Session
import time

# static urls
baseurl = 'https://api.discogs.com'
authorize_url = 'https://www.discogs.com/ja/oauth/authorize'

# your Discogs.com user name.
user = ''

# your Discogs.com API KEYS
consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

def list_get():
    auth = OAuth1(consumer_key, consumer_secret, access_token, access_secret)

    id_list = []
    cnt = []

    endpoint = baseurl + '/users/' + user + '/collection/folders/0/releases?per_page=100&page=1'
    r = requests.get(endpoint, auth=auth)
    result = json.loads(r.text)
    for results in result['releases']:
        releaseid = results['id']
        id_list.append(str(releaseid))
    
    permax = result['pagination']['pages'] + 1
    for cnt in range(2, permax):
        url = baseurl + '/users/' + user + '/collection/folders/0/releases?per_page=100&page=' + str(cnt)
        r = requests.get(url, auth=auth)
        result_url = json.loads(r.text)
        time.sleep(2)
        for results in result_url['releases']:
            releaseid = results['id']
            id_list.append(str(releaseid))

    choiceid = random.choice(id_list)
    print('releaseid: ' + choiceid)
    choice_endpoint = baseurl + '/releases/' + choiceid
    choice_r = requests.get(choice_endpoint, auth=auth)
    choice_result = json.loads(choice_r.text)
    artist_name = []
    for parse_artist in choice_result['artists']:
        artist_name.append(parse_artist['name'])
    artist_name_data = ", ".join(artist_name)
    title = choice_result['title']
    if not choice_result['thumb']:
        thumb = 'https://s.discogs.com/images/default-release.png'
    else:
        thumb = choice_result['thumb']
    uri = choice_result['uri']
    print('Artist name: ' + artist_name_data + '\nTitle: ' + title + '\nDiscogs URL: ' + uri + '\nThumbnail URL: ' + thumb)
    return artist_name_data, title, uri, thumb

def main():
    list_get()

if __name__ =='__main__':
    main()
