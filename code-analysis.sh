#!/bin/bash

function run_lint_checker {
    pylint $(find . -iname "*.py")
}


function run_report {
    local exit_code="$?"
    [[ ${exit_code} == 0 ]] && echo "Congratulation, your code is fully clear!" && exit 0
    [[ ${exit_code} == 0 ]] || echo "Some errors are occurred during coe assessment!" && exit 1
}


function run_code_assessment {
    run_lint_checker
    run_report
}


run_code_assessment
