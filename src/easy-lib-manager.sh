#!/usr/bin/env bash
echo "
            ███████ ██      ███    ███ 
            ██      ██      ████  ████ 
            █████   ██      ██ ████ ██ 
            ██      ██      ██  ██  ██ 
            ███████ ███████ ██      ██ 

            Easy Library Manager
 https://github.com/ALocalDeveloper/Easy-Lib-Manager
"

if [ $# -eq 0 ]; then
    echo "Usage: easy-lib-manager [command]"
    echo ""
    echo "Commands:"
    echo " download   Download libraries"
    echo " remove     Remove libraries"
    echo " list       List available libraries"
    echo " search     Search for a library"
    echo " exit       Exit the program"
    exit 0
fi

action=$1

case $action in
    download)
        python3 download_libraries.py
        ;;
    remove)
        python3 remove_libraries.py
        ;;
    list)
        python3 list_libraries.py
        ;;
    search)
        if [ $# -lt 2 ]; then
            echo "Enter the name or part of the name of the library you want to search for:"
            read query
        else
            query=$2
        fi
        python3 search.py "$query"
        ;;
    exit)
        exit 0
        ;;
    *)
        echo "Invalid action. Please enter 'download', 'remove', 'list', or 'search'."
        ;;
esac