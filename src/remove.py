import os
import shutil

def remove_libraries(libs):
    # Unset the CFLAGS, CXXFLAGS, and LDFLAGS environment variables
    del os.environ['CFLAGS']
    del os.environ['CXXFLAGS']
    del os.environ['LDFLAGS']

    # Delete the libraries
    for lib in libs:
        file_path = os.path.expanduser('~/') + lib.split('/')[-1]
        
        # Check if file exists
        if os.path.isfile(file_path):
            os.remove(file_path)
            print("Deleted file:", file_path)
        else:
            print("File does not exist:", file_path)

    # Remove the lib directory
    lib_dir = os.path.expanduser('~/lib')
    if os.path.isdir(lib_dir):
        shutil.rmtree(lib_dir)
        print("Deleted directory:", lib_dir)
    else:
        print("Directory does not exist:", lib_dir)

# Ask the user for the libraries they want to remove
libs = input("Enter the names of the libraries you want to remove, separated by spaces: ").split()

# Call the remove_libraries function
remove_libraries(libs)
