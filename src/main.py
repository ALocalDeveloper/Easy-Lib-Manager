import os
import requests

def setup_environment(libs):
    # Set the CFLAGS, CXXFLAGS, and LDFLAGS environment variables
    os.environ['CFLAGS'] = '-I/home/{}/include'.format(os.getlogin())
    os.environ['CXXFLAGS'] = '-I/home/{}/include'.format(os.getlogin())
    os.environ['LDFLAGS'] = '-L/home/{}/lib'.format(os.getlogin())

    # Download the libraries
    for lib in libs:
        download_file(lib)

def download_file(url):
    file_path = os.path.expanduser('~/') + url.split('/')[-1]
    
    # Check if file already exists
    if os.path.isfile(file_path):
        print("File already exists.")
        return

    response = requests.get(url)
    if response.status_code == 200:
        with open(file_path, 'wb') as f:
            f.write(response.content)

# Ask the user for the libraries they want to download
libs = input("Enter the URLs of the libraries you want to download, separated by spaces: ").split()

# Call the setup_environment function
setup_environment(libs)
