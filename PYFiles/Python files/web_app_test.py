import re,requests,sys,subprocess
try:
    from bs4 import BeautifulSoup
except ImportError:
    subprocess.call('python -m pip install beautifulsoup4')

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'}
url = input('Enter Url: ')
url_list=[]
javascript_files_list = []
def request(url):
    
    response = requests.get(url, headers=header)
    soup = BeautifulSoup(response.content)
    status = response.status_code
    javascript_files = [sc["src"] for sc in soup.find_all("script",src=True)]
    href_links = soup.find_all(href=True)
    for file in javascript_files:
        print(file)
        javascript_files_list.append(file)
    for link in href_links:
        print(link)
        url_list.append(link)
    
    if status == 200:
        if url not in url_list:
            url_list.append(url)


def print_list():
    for link in url_list:
        if url.strip("https://") in link:
            print("=" * 20 + "INSCOPE LINKS" + "="*20)
            print(link)


request(url=url)
print_list()



