#  choose at random from your collection on Discogs.com
Random release ID(with gets artist name, titles and thumbnail url) choice from your Discogs.com collections.   
Release ID get from your collections(Access to API. 1 access retrieve max 100 items.),Random choices from the results.   
   
I use it by twitterbot.

## configurations.(in discogs_random_get.py)
     17 # your Discogs.com user name.
     18 user = ''
     19
     20 # your Discogs.com API KEYS
     21 consumer_key = ''
     22 consumer_secret = ''
     23 access_token = ''
     24 access_secret = ''
## Sample
```
$ ./discogs_random_get.py
releaseid: 8891040
Artist name: Jody Watley
Title: Another Chapter
Discogs URL: https://www.discogs.com/Jody-Watley-Another-Chapter/release/8891040
Thumbnail URL: https://img.discogs.com/1ZwJqU1iFM6oadLidiAWCAYRCYw=/fit-in/150x150/filters:strip_icc():format(jpeg):mode_rgb():quality(40)/discogs-images/R-8891040-1474122336-2065.jpeg.jpg
$
```

## Requirement.
#### Pyhon3.X modules...
* requests
* requests_oauthlib

#### Registerd Discogs.com API key.
* registered Discogs application   
https://www.discogs.com/settings/developers

## License
MIT

