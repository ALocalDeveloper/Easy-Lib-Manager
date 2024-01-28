import sys
import json
import os

def search_libraries(query):
    print(f"Query: {query}") # Debugging line

    with open(os.path.join(os.path.dirname(__file__), 'libraries.json'), 'r') as f:
        libraries = json.load(f)

    query = query.lower()
    for key in libraries:
        if query in key.lower():
            print(f"{libraries[key]['name']} ({libraries[key]['version']}): {libraries[key]['link']}")
            return
    print("Library not found.")

if __name__ == "__main__":
    query = sys.argv[1]
    search_libraries(query)