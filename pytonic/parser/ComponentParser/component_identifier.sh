#!/usr/bin/env bash
is_workspace () {
    local workspace=$1
    local package=$(ls ${workspace}/src | head -n 1)
    if [[ -n "$package" ]]; then
        local package_sources=${workspace}/src/$package/src
        if [[ -d $package_sources ]]; then
            echo "${workspace##*/} ${workspace} workspace"
            exit 0
        fi
    fi
}

is_cmake_package () {
    local package=$1
    if [[ $(ls ${package} | awk ' /CMakeLists.txt/  {print}') ]]; then
        echo "${package##*/} ${package} cmake_package"
        exit 0
    fi
}

is_workspace $1
is_cmake_package $1