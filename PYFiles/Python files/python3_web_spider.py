try:
    import subprocess,re,base64,sys,socket,re,requests,time

except ImportError:
    print('Missing Depenecies')
    print('Installing requests Library')
    subprocess.call('python -m pip install requests')
    print('[+] Intall Completed \n Try Running {sys.argv[0]} again')

url = input('Enter Url: ')
link_dict = []
live_link = []
sleep_time = input('Enter time to sleep in tenths of a second between requests (example : 2 would be 0.2 seconds): ')
sleep_time = int(sleep_time)
sleep_time = sleep_time / 10

def request_url(url):
    response = requests.get(url, headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36"})
    print(response.status_code,flush=True)
    if response.status_code == 200:
        live_link.append(url)
        sys.stdout.flush()
        find_links(url=url,link_dict=link_dict,response=response)
    else:
        print( "[-]" + f"{url}" + str(response.status_code))



def find_links(url,link_dict,response):
    html = response.content
    links = re.findall(r'(?<=<a href=")[^"]*', str(html))
    for link in links:
        link = str(link).strip('\', \'http\')')
        link = str(link).strip('(\'')
        if link not in link_dict:
            if "http://" or "https://" not in link:
                link = url + "/" + link
                print(link)
            link_dict.append(link)
    



"""Function needs to be called to run"""
def spider(url):
    request_url(url=url)

    for link in link_dict:
        if "polkpa.org" in link:
            url = link
            request_url(url=url)
            time.sleep(sleep_time)
    
    clear()
    print("\n\n\n\n")
    print("In Scope Links\n")
    for link in link_dict:
        if str(url).strip("https://") in link:
            print(link)
    
    print("\n" + "="*20 + "\tHttp Response 200 OK Links\t" + "="*20)
    for link in live_link:
        print(link)

spider(url=url)
