#!/bin/bash

echo "What do you want to do? (download/remove/list)"
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
        python3 search.py
        ;;    
    *)
        echo "Invalid action."
        ;;
esac
