import http.client, urllib.request, urllib.parse, urllib.error, base64
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': 'beb49026b71748e797a0f5b8d1b2abe7',
}

# params = urllib.parse.urlencode({'en-US'})
f = open('phrases.txt','w')



try:
    conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn.request("GET", "/spid/v1.0/verificationPhrases?locale=en-US", "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    f.write(str(data))
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))