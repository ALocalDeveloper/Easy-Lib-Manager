#!/bin/bash

LIBS_DIR=~/libs

if [[ -d "$LIBS_DIR" ]]; then
    rm -rf "$LIBS_DIR"
fi

export LDFLAGS=${LDFLAGS#-L~/libs }
export CXXFLAGS=${CXXFLAGS#-I~/libs }

