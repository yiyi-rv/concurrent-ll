#!/bin/sh
set -x # print debug info

# This is running under Ubuntu 16.04
# Install necessary packages. 
sudo apt-get install -y libreadline-dev bc

export RVP_ANALYSIS_ARGS="--output=json" 
export RVP_REPORT_FILE="`pwd`/my_errors.json"


# Compile and run `lua`.
error_file=`pwd`/my_errors.json
compiler=rvpc
sudo make -j`nproc` CC=$compiler LD=$compiler 
rm $error_file

./rvscripts/rv0.sh


# Generate a HTML report with `rv-html-report` command,
# and output the HTML report to `./report` directory. 
rv-html-report $error_file -o report

# Upload your HTML report to RV-Toolkit website with `rv-upload-report` command. 
rv-upload-report `pwd`/report

# Done.
