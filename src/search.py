import requests
from html.parser import HTMLParser
from googlesearch import search
from urllib.parse import quote

class MyHTMLParser(HTMLParser):
    def __init__(self, j):
        super().__init__()
        self.j = j

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for name, value in attrs:
                if name == 'href' and ('download' in value and value.endswith(('tar', 'zip', 'tar.gz'))):
                    print(self.j.split('&')[0] + value)

def search_libraries(query):
    # Perform the search
    for ext in ['tar', 'zip', 'tar.gz']:
        for j in search(query + ' ' + ext, num_results=10):
            # Send a GET request to the URL
            response = requests.get(j)

            # Parse the HTML content of the page with Beautiful Soup
            parser = MyHTMLParser(j)
            parser.feed(str(response.content))

# Ask the user for the library they want to search for
query = input("Enter the name of the library you want to search for: ")

# Call the function
search_libraries(query)