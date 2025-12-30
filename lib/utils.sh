#!/usr/bin/env bash

die() {
    # Prints error message and exits
    echo "teevee: $*" >&2
    exit 1
}