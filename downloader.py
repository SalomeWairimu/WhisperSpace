import requests
import sys

def main():
    url = sys.argv[1]
    x = requests.head(url, allow_redirects=True)
    header = x.headers
    content_type = header.get('content-type')
    #use this format to specify allowable content types
    #if 'text' in content_type.lower():
    r = requests.get(url, allow_redirects=True)
    open('f.wav', 'wb').write(r.content)



main()
