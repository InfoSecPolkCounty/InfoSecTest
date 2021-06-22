try:
    import subprocess,re,base64,sys,socket,re,requests,time

except ImportError:
    print('Missing Depenecies')
    print('Installing requests Library')
    subprocess.call('python -m pip install requests')
    print('[+] Intall Completed \n Try Running {sys.argv[0]} again')

url = input('Enter Url: ')
link_dict = []
Live_OK_link=[]

def request_url(url):
    response = requests.get(url, headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36"})
    print(response.status_code)
    if response.status_code is 200:
        Live_OK_link.append(url)
        print( f"[+]\tFound Item {url}\t" + str(response.status_code) + "\tOK")
        find_links(url=url,link_dict=link_dict,response=response)
    else:
        print( "[-]" + f"{url}" + str(response.status_code))



def find_links(url,link_dict,response):
    html = response.content
    links = re.findall('"((http|ftp)s?://.*?)"', str(html))
    for link in links:
        link = str(link).strip('\', \'http\')')
        link = str(link).strip('(\'')
        print(link)
        link_dict.append(link)
    

"""Function needs to be called to run"""
def spider(url):
    request_url(url=url)

    for link in link_dict:
        if "polkpa.org" in link:
            url = link
            request_url(url=url)
            time.sleep(2)

    banner ="\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
    print(banner)
    for link in link_dict:
        if "polkpa" in link:
            print(link)
    print(banner)
    print("="*20 + "\tHttp Response 200 OK Links\t" + "="*20)
    for link in Live_OK_link:
        print(link)

spider(url=url)
