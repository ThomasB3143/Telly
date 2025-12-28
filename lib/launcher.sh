#!/usr/bin/env bash

find_launcher() {
    local name="$1"
    local user_path="$TELLY_USER_CONFIG/launchers/$name"
    local system_path="$TELLY_ROOT/launchers/$name"

    if [[ -d "$user_path" ]]; then
        validate_launcher "$user_path"
        echo "$user_path"
        return
    fi

    if [[ -d "$system_path" ]]; then
        validate_launcher "$system_path"
        echo "$system_path"
        return
    fi

    die "launcher '$name' not found"
}
