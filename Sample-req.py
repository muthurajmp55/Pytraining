import requests

class ApiError(Exception):
    def __int__(self,value):
        self.value=value

try:
    resp = requests.get('http://ap.plos.org/search?q=title:%22Drosophila%22%20and%20body:%22RNA%22&fl=id,abstract&wt=json&indent=on')
    if resp.status_code==200:
        print(resp.content)
except requests.ConnectionError as err:
    print(err)


