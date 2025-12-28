#!/usr/bin/env bash

die() {
    # Prints error message and exits
    echo "telly: $*" >&2
    exit 1
}