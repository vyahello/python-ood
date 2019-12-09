#!/bin/bash

declare -a RESULT

# specifies a set of variables to declare CLI output color
FAILED_OUT="\033[0;31m"
PASSED_OUT="\033[0;32m"
NONE_OUT="\033[0m"

# specifies a set of variables to declare files to be used for code assessment
PROJECT_FILES="./"

function store-failures {
    RESULT+=("$1")
}


function remove-pycache-trash {
    local PYCACHE_DIR="__pycache__"
    echo "Removing ${PYCACHE_DIR} directories if present ..."
    ( find . -d -name ${PYCACHE_DIR} | xargs rm -r ) || echo -e "No ${PYCACHE_DIR} found"
}


function remove-analysis-trash {
    local PYTEST_CACHE_DIR='.pytest_cache'
    local MYPY_CACHE_DIR='.mypy_cache'
    echo "Removing code analysis trash if present ..."
    [[ -d "$PYTEST_CACHE_DIR" ]] && rm -rf ${PYTEST_CACHE_DIR} && echo "pytest trash is removed"
    [[ -d "$MYPY_CACHE_DIR" ]] && rm -rf ${MYPY_CACHE_DIR} && echo "mypy trash is removed"
}


function install-dependencies {
   echo "Installing python code analysis packages ..." \
   && ( pip install --no-cache-dir --upgrade pip ) \
   && ( pip install --no-cache-dir -r requirements-dev.txt )
}


function run-unittests {
    echo "Running unittests ..." && ( pytest -m unittest )
}


function run-pylint-analysis() {
    echo "Running pylint analysis ..." && ( pylint $(find "${PROJECT_FILES}" -iname "*.py") )
}


function run-black-analysis() {
    echo "Running black analysis ..." && ( black --check "${PROJECT_FILES}" )
}


function run-code-analysis {
    echo "Running code analysis ..."
    remove-pycache-trash
    run-unittests || store-failures "Unittests are failed!"
    run-pylint-analysis || store-failures "pylint analysis is failed!"
    run-black-analysis || store-failures "black analysis is failed!"

    if [[ ${#RESULT[@]} -ne 0 ]];
        then echo -e "${FAILED_OUT}Some errors occurred while analysing the code quality.${NONE_OUT}"
        for failed_item in "${RESULT[@]}"; do
            echo -e "${FAILED_OUT}- ${failed_item}${NONE_OUT}"
        done
        remove-analysis-trash
        exit 1
    fi
    remove-analysis-trash
    echo -e "${PASSED_OUT}Code analysis is passed${NONE_OUT}"
}


function main() {
    if [[ "$1" == "install-dependencies" ]];
        then install-dependencies || store-failures "Python packages installation is failed!";
    fi
    run-code-analysis
}


main "$@"