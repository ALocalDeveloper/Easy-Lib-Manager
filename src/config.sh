#!/bin/bash

LIBS_DIR=~/libs

if [[ ! -d "$LIBS_DIR" ]]; then
    mkdir -p "$LIBS_DIR"
fi

export LDFLAGS="-L$LIBS_DIR $LDFLAGS"
export CXXFLAGS="-I$LIBS_DIR $CXXFLAGS"