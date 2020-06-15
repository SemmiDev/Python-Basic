import json
import urllib

url = "http://ajax.googleapis.com/ajax/services/feed/load?v=1.0#=100&q=http://feeds.feedburner.com/petanikode"
respon = urllib.urlopen(url)
data = json.loads(respon.read())

post = data['responseData']['feed']['entries']

for artikel in post:
    print(artikel['title'])