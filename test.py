import json
import requests

umbrellachannel_url = 'https://hooks.slack.com/services/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'
e = open('umbrella.txt', 'r')
message = e.readline()

response = requests.post(
   umbrellachannel_url, data=message,
    headers={'Content-Type': 'application/json'}
)
if response.status_code ==200:
   print response.status_code
   print response.text
else:
    raise ValueError(
        'Request failed %s, the response is:\n%s'
        % (response.status_code, response.text)
    )