# Easy-Lib-Manager
A library manager for c/c++ to make getting libraries working as fast and as easy as possible
config.sh will export the libs folder to the compiler so that it's automatically included and linked (you need to do source ./config.sh)
the library folder is located in ~/libs you will have to source config.sh every terminal session
if you want it to persist over terminal sessions you need to add source ./config.sh to your .bashrc or .bash_profile files
echo 'source /full/path/to/your/config.sh' >> ~/.bashrc

The search function only finds 64 bit .tar.gz or zip files for now

### THIS TOOL ONLY ADDS THE LIBS FOLDER TO THE COMPILER ARGS

### WORKS ONLY WITH GCC/Linux FOR NOW
## To use this you need:
Bash

GCC

python3

googlesearch python package

beautifulsoup python package

tqdm python package 

you can get this by running install.sh (for apt/debian based distros) or install-fedora.sh (for dnf/fedora)
##
### version 1.0.1
![Screenshot from 2024-01-28 17-32-51](https://github.com/ALocalDeveloper/Easy-Lib-Manager/assets/98947261/67b088c5-363a-41c8-8b6c-e1b5791bf23e)

### version 1.0.0
![Screenshot from 2024-01-26 21-15-56](https://github.com/ALocalDeveloper/Easy-Lib-Manager/assets/98947261/830e8a98-aa18-4f30-8e05-bda94b8af6a3)


