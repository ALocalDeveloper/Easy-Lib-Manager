import os

def list_libraries():
    libs_dir = os.path.expanduser('~/libs')
    libs = os.listdir(libs_dir)

    for lib in libs:
        print(lib)
