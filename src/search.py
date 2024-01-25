from googlesearch import search

def search_libraries(query):
    # Perform the search
    for j in search(query, num_results=10):
        print(j)

# Ask the user for the library they want to search for
query = input("Enter the name of the library you want to search for: ")

# Call the function
search_libraries(query)
