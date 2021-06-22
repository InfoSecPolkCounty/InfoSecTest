import requests
html_request = requests.get('https://polkpa.org')
print html_request.text
