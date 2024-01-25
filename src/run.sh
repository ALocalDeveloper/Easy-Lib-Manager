#!/bin/bash

echo "What do you want to do? (download/remove/list/search)"
read action

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
        echo "Enter the name or part of the name of the library you want to search for:"
        read query
        python3 search.py "$query"
        ;;
    *)
        echo "Invalid action. Please enter 'download', 'remove', 'list', or 'search'."
        ;;
esac
