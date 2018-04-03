import http.client, urllib.request, urllib.parse, urllib.error, base64, ssl
ssl._create_default_https_context = ssl._create_unverified_context

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': 'beb49026b71748e797a0f5b8d1b2abe7',
}

params = urllib.parse.urlencode({
})

myID = '4d4ea255-f00a-45c9-8ac1-353de0b2f859'

try:
    conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn.request("DELETE", "/spid/v1.0/verificationProfiles/{0}?".format(myID), "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))