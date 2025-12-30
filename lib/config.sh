#!/usr/bin/env bash

load_launcher_config() {
    local launcher_dir="$1"
    local config_file="$launcher_dir/launcher.conf"

    # Default values
    TIMEOUT_MS=1000
    OPTIONS=("$launcher_dir/options/"*.sh)
    HOVER_OPTIONS=("${OPTIONS[@]/#/ * }")
    TITLE="${launcher_dir}"
    SELECTED_TEXT=$OPTIONS


    # Source launcher.conf if exists
    if [[ -f "$config_file" ]]; then
        source "$config_file"
    fi
}

create_config() {
    local config_dir="$TEEVEE_USER_CONFIG"

    mkdir -p "$config_dir"

    echo "Initialised config directory at $config_dir"
}