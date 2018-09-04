#!/bin/bash
set -x
json_out=`pwd`/my_errors.json
report_out=`pwd`/report

# Install necessary packages 
apt install -y libreadline-dev bc

# Compile and run
export RVP_ANALYSIS_ARGS="--output=json" 
export RVP_REPORT_FILE=$json_out
make -j`nproc` CC=rvpc
rm $json_out

./rvscripts/rv0.sh

# Generate a HTML report with `rv-html-report` command,
# and output the HTML report to `./report` directory. 
rv-html-report $json_out -o $report_out

# Upload your HTML report to RV-Toolkit website with `rv-upload-report` command. 
rv-upload-report $report_out

# Done.
