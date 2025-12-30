#!/usr/bin/env bash

find_launcher() {
    # Checks if a launcher directory exists
    local name="$1"
    local user_path="$TEEVEE_USER_CONFIG/launchers/$name"
    local system_path="$TEEVEE_ROOT/launchers/$name"

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

validate_launcher() {
    # Checks if a launcher directory is valid
    local dir="$1"

    [[ -f "$dir/launcher.conf" ]] \
        || die "launcher missing launcher.conf: $dir"

    [[ -d "$dir/options" ]] \
        || die "launcher missing options directory: $dir"

    shopt -s nullglob
    local opts=("$dir/options/"*.sh)
    shopt -u nullglob

    (( ${#opts[@]} > 0 )) \
        || die "launcher has no option scripts: $dir"
}
