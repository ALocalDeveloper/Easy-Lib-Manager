import sys
import json

def search_libraries(query):
    print("Running search_libraries function") # Debugging line
    print(f"Query: {query}") # Debugging line

    with open('libraries.json', 'r') as f:
        libraries = json.load(f)

    query = query.lower()
    for key in libraries:
        if query in key.lower():
            print(libraries[key]['name'])
            print(libraries[key]['version'])
            print(libraries[key]['link'])
            return
    print("Library not found.")

if __name__ == "__main__":
    query = sys.argv[1]
    search_libraries(query)