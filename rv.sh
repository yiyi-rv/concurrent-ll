#!/bin/bash
set -x
json_out=`pwd`/my_errors.json
report_out=`pwd`/report

# Install necessary packages 
sudo apt-get install -y libreadline-dev bc

# Compile and run
compiler=rvpc
export RVP_ANALYSIS_ARGS="--output=json" 
export RVP_REPORT_FILE=$json_out
sudo make -j`nproc` CC=$compiler LD=$compiler 
rm $json_out

./rvscripts/rv0.sh

# Generate a HTML report with `rv-html-report` command,
# and output the HTML report to `./report` directory. 
rv-html-report $json_out -o $report_out

# Upload your HTML report to RV-Toolkit website with `rv-upload-report` command. 
rv-upload-report $report_out

# Done.
