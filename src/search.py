from bs4 import BeautifulSoup
import requests
from googlesearch import search

def search_libraries(query):
    # Perform the search
    for ext in ['tar', 'zip', 'tar.gz']:
        for j in search(query + ' ' + ext, num_results=10):
            # Send a GET request to the URL
            response = requests.get(j)

            # Parse the HTML content of the page with Beautiful Soup
            soup = BeautifulSoup(response.content, 'html.parser')

            # Find all <a> tags (which define hyperlinks)
            for a in soup.find_all('a'):
                # Check if the href attribute contains 'download' and ends with '.tar', '.zip', or '.tar.gz'
                if 'download' in a.get('href', '') and a['href'].endswith(ext):
                    print(a['href'])

# Ask the user for the library they want to search for
query = input("Enter the name of the library you want to search for: ")

# Call the function
search_libraries(query)