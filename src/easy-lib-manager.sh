#!/usr/bin/env bash

if [ $# -eq 0 ]; then
    echo "
             ███████ ██      ███    ███ 
             ██      ██      ████  ████ 
             █████   ██      ██ ████ ██ 
             ██      ██      ██  ██  ██ 
             ███████ ███████ ██      ██ 

                 Easy Library Manager
     https://github.com/ALocalDeveloper/Easy-Lib-Manager
    "
fi

if [ $# -eq 0 ]; then
    echo "Usage: easy-lib-manager [command]"
    echo ""
    echo "Commands:"
    echo " download   Download libraries"
    echo " remove     Remove libraries"
    echo " list       List available libraries"
    echo " search     Search for a library"
    echo " version    Display the version"
    exit 0
fi

action=$1

case $action in
    download)
        python3 "$(dirname "$0")/download_libraries.py"
        ;;
    remove)
        python3 "$(dirname "$0")/remove_libraries.py"
        ;;
    list)
        python3 "$(dirname "$0")/list_libraries.py"
        ;;
    search)
        if [ $# -lt 2 ]; then
            echo "Enter the name or part of the name of the library you want to search for:"
            read query
        else
            query=$2
        fi
        python3 "$(dirname "$0")/search.py" "$query"
        ;;
    version)
        echo "

             ███████ ██      ███    ███ 
             ██      ██      ████  ████ 
             █████   ██      ██ ████ ██ 
             ██      ██      ██  ██  ██ 
             ███████ ███████ ██      ██ 
        
               version v1.0.1-bugfix"
        ;;
    *)
        echo "Invalid action. Please enter 'download', 'remove', 'list', or 'search'."
        ;;
esac